from validation.types.type_validation import (
    ValidationType, ValidationTypeError
)
from uontypes.scalars.uon_float import UonFloat


class FloatTypeValidation(ValidationType):

    def validate_type(self, input_):
        if (not isinstance(input_, UonFloat)):
            raise ValidationTypeError("The following input {} type "
                                      "does not correspond to float"
                                      .format(input_))

    def __repr__(self):
        return "FloatTypeValidation()"

    def __str__(self):
        return "!float"

    def to_binary(self):
        """Binary representation of float type validation.

        b"\x22" corresponds to float type in UON.

        Returns:
            bytes: binary representation of float type validation
        """
        return b"\x22"
