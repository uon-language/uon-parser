import numpy as np

from uon_numeric import UonNumeric


class Integer32(UonNumeric):
    def __init__(self, value):
        v = np.int32(value)
        super().__init__(v, "int32", 32)


class Integer64(UonNumeric):
    def __init__(self, value):
        v = np.int64(value)
        super().__init__(v, "int64", 64)


class Integer128(UonNumeric):
    def __init__(self, value):
        """TODO: Convert the value to int 128"""
        super().__init__(value, "int128", 128)
