from validation.types.type_validation import (
    ValidationType, ValidationTypeError
)

from uonrevisedtypes.scalars.uon_url import UonUrl


class UrlTypeValidation(ValidationType):

    def validate_type(self, input_):
        if (not isinstance(input_, UonUrl)):
            raise ValidationTypeError(input_, "The following input {} type "
                                              "does not correspond to url"
                                              .format(input_))

    def __repr__(self):
        return "UrlTypeValidation()"

    def __str__(self):
        return "!url"

    def to_binary(self):
        """Binary representation of url type validation.

        b"\x4c" corresponds to UonUrl type in UON.

        Returns:
            bytes: binary representation of url type validation
        """
        return b"\x4c"
