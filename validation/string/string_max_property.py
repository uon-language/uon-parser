from validation.string.string_property_validation import (
    StringPropertiesValidation)
from validation.property import ValidationPropertyError


class MaxStringValidation(StringPropertiesValidation):
    def __init__(self, maximum):
        self.maximum = maximum

    def validate_property(self, input):
        if (len(input.value) < self.maximum):
            raise MaxStringValidationError(input, """The following input {}
                                           has length bigger than {}"""
                                           .format(input, self.maximum))
    
    def __repr__(self):
        return "MaxStringValidation({})".format(self.maximum)


class MaxStringValidationError(ValidationPropertyError):
    def __init__(self, expression, message):
        super().__init(expression, message)
