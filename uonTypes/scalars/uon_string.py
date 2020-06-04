from uonTypes.scalars.uon_scalar import UonScalar


class UonString(UonScalar):
    def __init__(self, value, uon_type, unit):
        super().__init__(value, uon_type)
        self.uon_type = "str"
