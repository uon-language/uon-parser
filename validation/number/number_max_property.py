from validation.number.number_property_validation import (
    NumberPropertiesValidation)
from validation.property import ValidationPropertyError


class MaxNumberValidation(NumberPropertiesValidation):
    def __init__(self, maximum):
        self.maximum = maximum

    def validate_property(self, input):
        if (input.value > self.maximum):
            raise MaxNumberValidationError(input, """The following input {}
                                           is bigger than {}"""
                                           .format(input, self.maximum))

    def __repr__(self):
        return "MaxNumberValidation({})".format(self.maximum)


class MaxNumberValidationError(ValidationPropertyError):
    def __init__(self, expression, message):
        super().__init(expression, message)
