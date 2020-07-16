from uonrevisedtypes.uon_base import UonBase


class UonNull(UonBase):
    def __init__(self, presentation_properties={}):
        super().__init__(None, "null", presentation_properties)

    def __str__(self):
        return "null"

    def __repr__(self):
        return "UonNull()"

    def to_binary(self):
        return b"\x02"
