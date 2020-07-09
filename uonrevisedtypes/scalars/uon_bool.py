from uonrevisedtypes.scalars.uon_scalar import UonScalar


class UonBoolean(UonScalar):
    def __init__(self, value, presentation_properties={}):
        super().__init__(value, "bool", presentation_properties)

    def __repr__(self):
        return "UonBoolean({})".format(self.value)

    def to_binary(self):
        return b"\x00"
