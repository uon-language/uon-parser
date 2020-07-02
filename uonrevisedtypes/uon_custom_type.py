from uonrevisedtypes.uon_base import UonBase


class UonCustomType(UonBase):
    def __init__(self, type_, attributes):
        super().__init__()
        self.type_ = type_
        self.attributes = attributes

    def __repr__(self):
        return "UonCustomType({}, {})".format(
            self.type_, self.attributes
        )
