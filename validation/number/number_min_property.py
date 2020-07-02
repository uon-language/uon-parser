from validation.number.number_property_validation import (
    NumberPropertiesValidation)
from validation.property import ValidationPropertyError


class MinNumberValidation(NumberPropertiesValidation):
    """
    An example of a validation property. This property verifies
    a numeric input's value is bounded by a certain minimum.
    """
    def __init__(self, minimum):
        self.minimum = minimum

    def validate_property(self, input):
        if (input.value < self.minimum):
            raise MinNumberValidationError(input, """The following input {}
                                           is smaller than {}"""
                                           .format(input, self.minimmum))

    def __repr__(self):
        return "MinNumberValidation({})".format(self.minimum)


class MinNumberValidationError(ValidationPropertyError):
    def __init__(self, expression, message):
        super().__init(expression, message)
