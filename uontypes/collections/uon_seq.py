import pprint

from uontypes.uon_value import UonValue

from binary.utils import EOL


class UonSeq(UonValue):
    def __init__(self, seq=[], presentation_properties={}):
        if seq is None:
            seq = []
        super().__init__(seq, "seq", presentation_properties)

    def get(self, index):
        return self.value[index]

    def append_(self, new_value):
        self.value.append_(new_value)

    def __eq__(self, other):
        if isinstance(other, UonSeq):
            return self.value == other.value
        return NotImplemented

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return '[%s]' % ', '.join(map(str, self.value))

    def __repr__(self):
        return "UonSeq({})".format(pprint.pformat(self.value))

    def to_binary(self):
        encoded_seq = b""
        for v in self.value:
            encoded_seq += v.to_binary()
        return b"\x01" + encoded_seq + EOL
