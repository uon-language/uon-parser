from uonrevisedtypes.uon_base import UonBase


class UonCustomType(UonBase):
    def __init__(self, type_):
        super().__init__()
        self.type_ = type_
