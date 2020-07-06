import numpy as np

from uonrevisedtypes.scalars.uon_numeric import UonNumeric


class UonFloat(UonNumeric):
    def __init__(self, value, uon_type, precision):
        super().__init__(value, uon_type, precision)


class Float32(UonFloat):
    def __init__(self, value):
        v = np.float32(value)
        super().__init__(v, "float32", 32)

    def __repr__(self):
        return "Float32(self, {}, {}, {}".format(
            self.value, self.uon_type, self.precision)

    def to_binary(self):
        return b"\x00"


class Float64(UonFloat):
    def __init__(self, value):
        v = np.float64(value)
        super().__init__(v, "float64", 64)

    def __repr__(self):
        return "Float64(self, {}, {}, {}".format(
            self.value, self.uon_type, self.precision)

    def to_binary(self):
        return b"\x00"


class Float128(UonFloat):
    def __init__(self, value):
        v = np.float128(value)
        super().__init__(v, "float128", 128)

    def __repr__(self):
        return "Float128(self, {}, {}, {}".format(
            self.value, self.uon_type, self.precision)

    def to_binary(self):
        return b"\x00"


# l = [Float32, Float64, Float128]
# for f in l:
#     print(f.__name__,   f(3.02))
