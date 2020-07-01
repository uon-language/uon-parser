from validation.number.number_property_validation import NumberValidation
from validation.property import ValidationPropertyError


class MinNumberValidation(NumberValidation):
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


class MinNumberValidationError(ValidationPropertyError):
    def __init__(self, expression, message):
        super().__init(expression, message)
