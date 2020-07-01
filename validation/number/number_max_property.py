from validation.number.number_property_validation import NumberValidation
from validation.property import ValidationPropertyError


class MaxNumberValidation(NumberValidation):
    def __init__(self, maximum):
        self.maximum = maximum

    def validate_property(self, input):
        if (input.value > self.maximum):
            raise MaxNumberValidationError(input, """The following input {}
                                           is bigger than {}"""
                                           .format(input, self.maximum))


class MaxNumberValidationError(ValidationPropertyError):
    def __init__(self, expression, message):
        super().__init(expression, message)
