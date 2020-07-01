import numpy as np

from uonrevisedtypes.scalars.uon_numeric import UonNumeric


class Uint32(UonNumeric):
    def __init__(self, value):
        v = np.uint32(value)
        super().__init__(v, "uint32", 32)

    def __repr__(self):
        return "Uint32(self, {}, {}, {}".format(
            self.value, self.uon_type, self.precision)


class Uint64(UonNumeric):
    def __init__(self, value):
        v = np.uint64(value)
        super().__init__(v, "uint64", 64)

    def __repr__(self):
        return "Uint64(self, {}, {}, {}".format(
            self.value, self.uon_type, self.precision)


class Uint128(UonNumeric):
    def __init__(self, value):
        """TODO: Convert the value to int 128"""
        super().__init__(value, "uint128", 128)

    def __repr__(self):
        return "Uint128(self, {}, {}, {}".format(
            self.value, self.uon_type, self.precision)
