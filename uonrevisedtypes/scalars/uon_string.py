from uonrevisedtypes.scalars.uon_scalar import UonScalar

from binary.utils import encode_string, STRING_LENGTH_MAX_VALUE

# TODO: maybe inherit from string also?
class UonString(UonScalar):
    def __init__(self, value, presentation_properties={}):
        if len(value) > STRING_LENGTH_MAX_VALUE:
            raise ValueError(("Uon strings cannot have a length "
                              f"of more than {STRING_LENGTH_MAX_VALUE} "
                              "characters"))
        super().__init__(value, "str", presentation_properties)

    def __len__(self):
        return len(self.value)

    def __str__(self):
        return f"!str {self.value}"

    def __repr__(self):
        return "UonString({})".format(self.value)

    def __eq__(self, other):
        if isinstance(other, UonString):
            return self.value == other.value
        return NotImplemented

    def __hash__(self):
        return hash(self.value)

    def to_binary(self):
        """Encode the string value in binary using utf-8
        as well as its length (valuable info when decoding 
        later on). Length will be encoded as an unsigned
        short (max 65535).
        """
        return b"\x11" + encode_string(self.value)
