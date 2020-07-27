import struct

from validation.properties.string.string_property_validation import (
    StringPropertiesValidation)
from validation.properties.property import ValidationPropertyError


class MinStringValidation(StringPropertiesValidation):
    def __init__(self, minimum):
        self.minimum = minimum

    def validate_property(self, input_):
        if (len(input_) < self.minimum):
            raise MinStringValidationError("The following input {} "
                                           "has length smaller than {}"
                                           .format(input_, self.minimum))

    def __repr__(self):
        return "MinStringValidation({})".format(self.minimum)

    def __str__(self):
        return f"min: {self.minimum}"

    def to_binary(self):
        """Binary representation of string max property.

        Concatenate the min keyword (\0x7) to \x11 reserved for 
        string types.

        String length is encoded on an unsigned short.
        
        Returns:
            bytes: binary representation of string max property
        """
        return b"\x11\x07" + struct.pack("<H", self.minimum)


class MinStringValidationError(ValidationPropertyError):
    pass
