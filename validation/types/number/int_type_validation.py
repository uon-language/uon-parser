from validation.types.type_validation import (
    ValidationType, ValidationTypeError
)
from uonrevisedtypes.scalars.uon_integer import UonInteger


class IntegerTypeValidation(ValidationType):

    def validate_type(self, input_):
        if (not isinstance(input_, UonInteger)):
            raise ValidationTypeError("The following input {} type "
                                      "does not correspond to integer"
                                      .format(input_))

    def __repr__(self):
        return "IntegerTypeValidation()"

    def __str__(self):
        return "!int"

    def to_binary(self):
        """Binary representation of integer type validation.

        b"\x29" corresponds to integer type in UON.

        Returns:
            bytes: binary representation of integer type validation
        """
        return b"\x29"
