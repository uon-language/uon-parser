from uonTypes.scalars.uon_scalar import UonScalar


class UonString(UonScalar):
    def __init__(self, value):
        super().__init__(value)
        self.uon_type = "str"
