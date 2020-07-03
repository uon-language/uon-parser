from validation.string.string_property_validation import (
    StringPropertiesValidation)
from validation.property import ValidationPropertyError


class MaxStringValidation(StringPropertiesValidation):
    def __init__(self, maximum):
        self.maximum = maximum

    def validate_property(self, input_):
        if (len(input_) > self.maximum):
            raise MaxStringValidationError(input_, """The following input {}
         has length bigger than {}""".format(input_, self.maximum))
    
    def __repr__(self):
        return "MaxStringValidation({})".format(self.maximum)


class MaxStringValidationError(ValidationPropertyError):
    def __init__(self, expression, message):
        super().__init__(expression, message)
