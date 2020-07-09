import pprint


class Schema:
    '''
    TODO: Need to add UUID
    '''
    def __init__(self, type_, validators):
        """
        A Schema defines a type with a list of attributes. 
        Attributes have to verify certain properties. So it's 
        fitting to store them in a dictionary where the attributes 
        serve as keys and the properties they have to verify serve as 
        values.

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
        return "Schema({}, {})".format(
            self.type_, pprint.pformat(self.validators)
        )

    def __str__(self):
        return "!!{}: {}".format(
            self.type_, pprint.pformat(self.validators)
        )


class RequiredAttributeError(Exception):
    pass
