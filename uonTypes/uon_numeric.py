from uonTypes.uon_scalar import UonScalar


class UonNumeric(UonScalar):
    def __init__(self, value, uon_type, precision):
        super().__init__(value, uon_type)
        self.precision = precision

    def __repr__(self):
        return "UonNumeric(self, {}, {}, {}".format(
            self.value, self.uon_type, self.precision)
    
    def __str__(self):
        return "!!{} {}".format(self.uon_type, self.value)
