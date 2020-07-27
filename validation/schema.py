import pprint

from uon import Uon
from binary.utils import encode_string, EOL
from validation.validator import ValidationError


class Schema(Uon):
    '''
    TODO: Need to add UUID
    '''
    def __init__(self, type_, validators={}, name=None,
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
        if (validators is None):
            validators = {}
        self.type_ = type_
        self.name = name
        if name is None:
            self.name = self.type_
        self.description = description
        self.uuid = uuid
        self.validators = validators
        self.required_attributes = []
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
            try:
                self.validators[k].validate(v)
            except ValidationError as e:
                message = (f"Validation error occured at attribute {k} "
                           f"in schema !!{self.type_}")
                raise ValidationError(message) from e
    
    def __repr__(self):
        return "Schema({!r}, {}, {!r}, {!r}, {!r})".format(
            self.type_, pprint.pformat(self.validators),
            self.name, self.description, self.uuid
        )

    def __str__(self):
        # validators_to_string = {k: str(v) for k, v in self.validators.items()}
        # pprint.pformat(validators_to_string)
        validators_to_string = '{'+', '.join(
            [': '.join(map(str, k)) for k in self.validators.items()])+'}'
        return ("!!{}: !schema("
                "name: {}, "
                "description: {}, "
                "uuid: {}) {}").format(
            self.type_, self.name, self.description,
            self.uuid, 
            validators_to_string
        )

    def to_binary(self):
        """Return the binary representation of a schema.

        First we encode the custom type (that the schema defines) name.

        Then we encode the presentation properties of a schema such as its 
        name, description, and uuid. Since name, description and uuid here
        are not keywords, they have no corresponding binary encoding to 
        identify them when decoding. So they are encoded as strings, in order,
        and if one is None it is encoded to \x00.

        Finally follows the encoding of the validators stored in a dictionary.
        Each attribute has a validator. The attribute (the key) is encoded as
        a keyname in a dictionary and the validator(the value) is encoded 
        using its own to_binary() method (Refer to UonMapping to_binary()).

        Finally the byte b"\x18" denotes the beginning of a schema

        Returns:
            bytes: Binary representation of a UON schema
        """
        name_encoded = (b"\x00" if self.name is None
                        else b"\x11" + encode_string(self.name))
        description_encoded = (b"\x00" if self.description is None
                               else b"\x11" + encode_string(self.description))
        uuid_encoded = (b"\x00" if self.uuid is None
                        else self.uuid.to_binary())
        validators_to_binary = b""
        for k, v in self.validators.items():
            validators_to_binary += (b"\x12"
                                     + encode_string(k)
                                     + v.to_binary())
        return (b"\x18" + encode_string(self.type_)
                        + name_encoded + description_encoded + uuid_encoded
                        + validators_to_binary
                        + EOL)


class RequiredAttributeError(Exception):
    pass
