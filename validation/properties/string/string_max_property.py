import struct

from validation.properties.string.string_property_validation import (
    StringPropertiesValidation)
from validation.properties.property import ValidationPropertyError

from binary.utils import STRING_LENGTH_MAX_VALUE


class MaxStringValidation(StringPropertiesValidation):
    def __init__(self, maximum):
        if maximum > STRING_LENGTH_MAX_VALUE:
            raise ValueError(("Uon strings cannot have a length "
                              f"of more than {STRING_LENGTH_MAX_VALUE} "
                              "characters"))
        self.maximum = maximum

    def validate_property(self, input_):
        if (len(input_) > self.maximum):
            raise MaxStringValidationError("The following input {} "
                                           "has length bigger than {}"
                                           .format(input_, self.maximum))
    
    def __repr__(self):
        return "MaxStringValidation({})".format(self.maximum)

    def __str__(self):
        return f"max: {self.maximum}"

    def to_binary(self):
        """Binary representation of string max property.

        Concatenate the max keyword (\0x8) to \x11 reserved for 
        string types.

        String length is encoded on an unsigned short.
        
        Returns:
            bytes: binary representation of string max property
        """
        return b"\x11\x08" + struct.pack("<H", self.maximum)


# TODO: try dynamically generating exception classes in the class above
class MaxStringValidationError(ValidationPropertyError):
    pass
