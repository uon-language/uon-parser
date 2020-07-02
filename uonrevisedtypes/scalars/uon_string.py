from uonrevisedtypes.scalars.uon_scalar import UonScalar


class UonString(UonScalar):
    def __init__(self, value):
        super().__init__(value, "str")

    def __repr__(self):
        return "UonString({})".format(self.value)
