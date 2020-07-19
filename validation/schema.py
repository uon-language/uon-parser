import pprint

from binary.utils import encode_string


class Schema:
    '''
    TODO: Need to add UUID
    '''
    def __init__(self, type_, validators, name=None,
                 description=None, uuid=None):
        """
        A Schema defines a type with a list of attributes. 
        Attributes have to verify certain properties. So it's 
        fitting to store them in a dictionary where the attributes 
        serve as keys and the properties they have to verify serve as 
        values. By default its name is the same as its type.

        example: 
        Schema(person, 
               {'age': Validator(UintTypeValidation(), 
                       [MinNumberValidation(0.0), MaxNumberValidation(125.0)],
                        {}),
                'minor': Validator(BooleanTypeValidation(), {}, {}),
                'name': Validator(StringTypeValidation(), 
                        [MinStringValidation(3), MaxStringValidation(25)], 
                        {'description': 'name of the person'})
                })
        """
        self.type_ = type_
        self.validators = validators
        self.required_attributes = []
        self.name = name
        if name is None:
            self.name = self.type_
        self.description = description
        self.uuid = uuid
        for attribute, validator in validators.items():
            optional = validator.presentation_properties.get('optional')
            if optional is not None and not optional:
                self.required_attributes.append(attribute)

    def validateSchema(self, input_):
        """
        Takes a UonCustomType and validates it. A UonCustomType
        has a UonMapping as attributes.
        First validates that all required attributes are present.
        Then for each attribute apply the validation with their corresponding
        validator.
        """
        attributes_mapping = input_.attributes.value
        for k in self.required_attributes:
            try:
                attributes_mapping[k]
            except KeyError:
                raise RequiredAttributeError("Required attribute {} "
                                             "missing".format(k))

        for k, v in attributes_mapping.items():
            self.validators[k].validate(v)
    
    def __repr__(self):
        return "Schema({}, {}, {}, {}, {})".format(
            self.type_, pprint.pformat(self.validators),
            self.name, self.description, self.uuid
        )

    def __str__(self):
        return ("!!{}: !schema("
                "name: {}, "
                "description: {}, "
                "uuid: {}) {}").format(
            self.type_, self.name, self.description,
            self.uuid, pprint.pformat(self.validators)
        )

    def to_binary(self):
        name_encoded = (b"\x00" if self.name is None
                        else encode_string(self.name))
        description_encoded = (b"\x00" if self.description is None
                               else encode_string(self.description))
        uuid_encoded = (b"\x00" if self.uuid is None
                        else encode_string(self.uuid))
        return b"\x18" + name_encoded + description_encoded + uuid_encoded


class RequiredAttributeError(Exception):
    pass
