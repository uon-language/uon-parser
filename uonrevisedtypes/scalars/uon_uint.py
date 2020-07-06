import numpy as np

from uonrevisedtypes.scalars.uon_numeric import UonNumeric


class UonUint(UonNumeric):
    def __init__(self, value, uon_type, precision):
        super().__init__(value, uon_type, precision)


class Uint32(UonUint):
    def __init__(self, value):
        v = np.uint32(value)
        super().__init__(v, "uint32", 32)

    def __repr__(self):
        return "Uint32(self, {}, {}, {}".format(
            self.value, self.uon_type, self.precision)

    def to_binary(self):
        return b"\x00"


class Uint64(UonUint):
    def __init__(self, value):
        v = np.uint64(value)
        super().__init__(v, "uint64", 64)

    def __repr__(self):
        return "Uint64(self, {}, {}, {}".format(
            self.value, self.uon_type, self.precision)

    def to_binary(self):
        return b"\x00"


class Uint128(UonUint):
    def __init__(self, value):
        """TODO: Convert the value to int 128"""
        super().__init__(value, "uint128", 128)

    def __repr__(self):
        return "Uint128(self, {}, {}, {}".format(
            self.value, self.uon_type, self.precision)

    def to_binary(self):
        return b"\x00"
