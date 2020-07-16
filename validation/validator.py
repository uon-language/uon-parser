import pprint


class Validator:
    def __init__(self, type_validation, properties_validations,
                 presentation_properties={}):
        self.type_validation = type_validation
        self.properties_validations = properties_validations
        self.presentation_properties = presentation_properties

    def validate(self, input_):
        self.type_validation.validate_type(input_)
        for property_validation in self.properties_validations:
            property_validation.validate_property(input_)

    def __repr__(self):
        return "Validator({}, {}, {})".format(
            self.type_validation, pprint.pformat(self.properties_validations),
            self.presentation_properties)


class ValidationError(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
