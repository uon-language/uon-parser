from validation.types.type_validation import (
    ValidationType, ValidationTypeError
)
from uontypes.scalars.uon_bool import UonBoolean


class BooleanTypeValidation(ValidationType):

    def validate_type(self, input_):
        if (not isinstance(input_, UonBoolean)):
            raise ValidationTypeError("The following input {} type "
                                      "does not correspond to boolean"
                                      .format(input_))

    def __repr__(self):
        return "BooleanTypeValidation()"

    def __str__(self):
        return "!bool"

    def to_binary(self):
        """Binary representation of boolean type validation.

        b"\x14" corresponds to UonBoolean type in UON.

        Returns:
            bytes: binary representation of boolean type validation
        """
        return b"\x14"
