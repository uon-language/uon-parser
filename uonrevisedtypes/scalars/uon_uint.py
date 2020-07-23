import numpy as np

from uonrevisedtypes.scalars.uon_integer import UonInteger


class UonUint(UonInteger):
    def __init__(self, value, uon_type, precision, unit=None,
                 presentation_properties={}):
        super().__init__(value, uon_type, precision, unit,
                         presentation_properties)


class Uint32(UonUint):
    def __init__(self, value, unit=None, presentation_properties={}):
        v = np.uint32(value)
        super().__init__(v, "uint32", 32, unit, presentation_properties)

    def to_binary(self):
        return b"\x39" + self.value.tobytes()


class Uint64(UonUint):
    def __init__(self, value, unit=None, presentation_properties={}):
        v = np.uint64(value)
        super().__init__(v, "uint64", 64, unit, presentation_properties)

    def to_binary(self):
        return b"\x3a" + self.value.tobytes()


class Uint128(UonUint):
    def __init__(self, value, unit=None, presentation_properties={}):
        """TODO: Convert the value to int 128"""
        super().__init__(value, "uint128", 128, unit, presentation_properties)

    def to_binary(self):
        return b"\x3b" + self.value.tobytes()
