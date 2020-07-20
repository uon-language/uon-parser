from validation.types.type_validation import (
    ValidationType, ValidationTypeError
)
from uonrevisedtypes.scalars.uon_integer import UonInteger


class IntegerTypeValidation(ValidationType):

    def validate_type(self, input_):
        if (not isinstance(input_, UonInteger)):
            raise ValidationTypeError(input_, "The following input {} type "
                                              "does not correspond to integer"
                                              .format(input_))

    def __repr__(self):
        return "IntegerTypeValidation()"

    def __str__(self):
        return "!int"
