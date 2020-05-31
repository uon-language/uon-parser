import numpy as np

from uon_numeric import UonNumeric


class Float32(UonNumeric):
    def __init__(self, value):
        v = np.float32(value)
        super().__init__(v, "float32", 32)


class Float64(UonNumeric):
    def __init__(self, value):
        v = np.float64(value)
        super().__init__(v, "float64", 64)


class Float128(UonNumeric):
    def __init__(self, value):
        v = np.float128(value)
        super().__init__(v, "float128", 128)
