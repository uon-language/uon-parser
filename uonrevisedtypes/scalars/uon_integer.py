import numpy as np

from uonrevisedtypes.scalars.uon_numeric import UonNumeric


class UonInteger(UonNumeric):
    def __init__(self, value, uon_type, precision, presentation_properties={}):
        super().__init__(value, uon_type, precision, presentation_properties)


class Integer32(UonInteger):
    def __init__(self, value, presentation_properties={}):
        v = np.int32(value)
        super().__init__(v, "int32", 32, presentation_properties)

    def __repr__(self):
        return "Integer32(self, {}, {}, {})".format(
            self.value, self.uon_type, self.precision)

    def to_binary(self):
        return b"\x00"


class Integer64(UonInteger):
    def __init__(self, value, presentation_properties={}):
        v = np.int64(value)
        super().__init__(v, "int64", 64, presentation_properties)

    def __repr__(self):
        return "Integer64(self, {}, {}, {})".format(
            self.value, self.uon_type, self.precision)

    def to_binary(self):
        return b"\x00"


class Integer128(UonInteger):
    def __init__(self, value, presentation_properties={}):
        """TODO: Convert the value to int 128"""
        super().__init__(value, "int128", 128, presentation_properties)

    def __repr__(self):
        return "Integer128(self, {}, {}, {})".format(
            self.value, self.uon_type, self.precision)

    def to_binary(self):
        return b"\x00"
