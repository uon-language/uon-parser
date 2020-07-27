import struct 

from validation.properties.number.number_property_validation import (
    NumberPropertiesValidation)
from validation.properties.property import ValidationPropertyError


class MinNumberValidation(NumberPropertiesValidation):
    """
    An example of a validation property. This property verifies
    a numeric input_'s value is bounded by a certain minimum.
    """
    def __init__(self, minimum):
        self.minimum = minimum

    def validate_property(self, input_):
        if (input_.value < self.minimum):
            raise MinNumberValidationError("The following input {} "
                                           "is smaller than {}"
                                           .format(input_, self.minimum))

    def __repr__(self):
        return "MinNumberValidation({})".format(self.minimum)

    def __str__(self):
        return f"min: {self.minimum}"

    def to_binary(self):
        """Binary representation of number min property.

        Concatenate the min keyword (\0x7) to \x15 reserved for 
        numeric types.

        Numeric ranges are encoded on a double precision float.
        
        Returns:
            bytes: binary representation of number min property
        """
        return b"\x15\x07" + struct.pack("<d", self.minimum)


class MinNumberValidationError(ValidationPropertyError):
    pass
