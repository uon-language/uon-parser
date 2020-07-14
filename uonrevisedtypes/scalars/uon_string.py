import struct

from uonrevisedtypes.scalars.uon_scalar import UonScalar

# TODO: maybe inherit from string also?
class UonString(UonScalar):
    def __init__(self, value, presentation_properties={}):
        super().__init__(value, "str", presentation_properties)

    def __len__(self):
        return len(self.value)

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
        encoded = self.value.encode("utf-8")
        length = len(encoded)
        length_encoded = struct.pack("<H", length)
        return b"\x11" + length_encoded + encoded
