from validation.string.string_property_validation import StringValidation
from validation.property import ValidationPropertyError


class MaxStringValidation(StringValidation):
    def __init__(self, maximum):
        self.maximum = maximum

    def validate_property(self, input):
        if (len(input.value) < self.maximum):
            raise MaxStringValidationError(input, """The following input {}
                                           has length bigger than {}"""
                                           .format(input, self.maximum))


class MaxStringValidationError(ValidationPropertyError):
    def __init__(self, expression, message):
        super().__init(expression, message)
