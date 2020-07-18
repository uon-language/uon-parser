from uonrevisedtypes.scalars.uon_scalar import UonScalar

from binary.utils import encode_string


class UonUrl(UonScalar):
    def __init__(self, value, presentation_properties={}):
        super().__init__(value, presentation_properties)

    def __repr__(self):
        return f"UonUrl({self.value})"

    def __str__(self):
        return f"!url {self.value}"

    def __eq__(self, other):
        if isinstance(other, UonUrl):
            return self.value == other.value
        return NotImplemented

    def __hash__(self):
        return hash(self.value)

    def to_binary(self):
        return b"\x4c" + encode_string(self.value)
