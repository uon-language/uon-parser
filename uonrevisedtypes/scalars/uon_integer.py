import numpy as np

from uonrevisedtypes.scalars.uon_float import UonFloat


class UonInteger(UonFloat):
    def __init__(self, value, uon_type, precision, unit=None,
                 presentation_properties={}):
        super().__init__(value, uon_type, precision, unit,
                         presentation_properties)


class Integer32(UonInteger):
    def __init__(self, value, unit=None, presentation_properties={}):
        v = np.int32(value)
        super().__init__(v, "int32", 32, unit, presentation_properties)
    
    def to_binary(self):
        return b"\x33" + super().to_binary()


class Integer64(UonInteger):
    def __init__(self, value, unit=None, presentation_properties={}):
        v = np.int64(value)
        super().__init__(v, "int64", 64, unit, presentation_properties)

    def to_binary(self):
        return b"\x34" + super().to_binary()


class Integer128(UonInteger):
    def __init__(self, value, unit=None, presentation_properties={}):
        """TODO: Convert the value to int 128"""
        super().__init__(value, "int128", 128, unit, presentation_properties)

    def to_binary(self):
        return b"\x35" + super().to_binary()
