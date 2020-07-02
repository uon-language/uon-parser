from validation.string.string_property_validation import (
    StringPropertiesValidation)
from validation.property import ValidationPropertyError


class MinStringValidation(StringPropertiesValidation):
    def __init__(self, minimum):
        self.minimum = minimum

    def validate_property(self, input):
        if (len(input.value) < self.minimum):
            raise MinStringValidationError(input, """The following input {}
                                           has length smaller than {}"""
                                           .format(input, self.minimmum))

    def __repr__(self):
        return "MinStringValidation({})".format(self.minimum)


class MinStringValidationError(ValidationPropertyError):
    def __init__(self, expression, message):
        super().__init(expression, message)
