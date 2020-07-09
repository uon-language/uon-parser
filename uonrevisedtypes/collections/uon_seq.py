import pprint

from uonrevisedtypes.uon_base import UonBase


class UonSeq(UonBase):
    def __init__(self, seq, presentation_properties={}):
        super().__init__(seq, "seq", presentation_properties)

    def __str__(self):
        return pprint.pformat(self.seq)

    def __repr__(self):
        return "UonSeq({})".format(pprint.pformat(self.seq))
