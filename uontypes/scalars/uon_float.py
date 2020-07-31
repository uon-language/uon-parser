import numpy as np

from uontypes.scalars.uon_numeric import UonNumeric


class UonFloat(UonNumeric):
    """A Uon type to represent floats.
    In reality, the float represented by this class are what
    we refer to as decimal real in the uon specification.
    """
    def __init__(self, value, uon_type, precision, unit=None,
                 presentation_properties={}):
        super().__init__(value, uon_type, precision, unit,
                         presentation_properties)


class Float16(UonFloat):
    """
    https://stackoverflow.com/questions/38975770/python-numpy-float16-datatype-operations-and-float8
    """
    pass


class Float32(UonFloat):
    def __init__(self, value, unit=None, presentation_properties={}):
        v = np.float32(value)
        super().__init__(v, "float32", 32, unit, presentation_properties)

    def to_binary(self):
        return b"\x23" + super().to_binary()


class Float64(UonFloat):
    def __init__(self, value, unit=None, presentation_properties={}):
        v = np.float64(value)
        super().__init__(v, "float64", 64, unit, presentation_properties)

    def to_binary(self):
        return b"\x24" + super().to_binary()


class Float128(UonFloat):
    def __init__(self, value, unit=None, presentation_properties={}):
        v = np.float128(value)
        super().__init__(v, "float128", 128, unit, presentation_properties)

    def to_binary(self):
        return b"\x25" + super().to_binary()
