class UonCustomType:
    def __init__(self, type_, attributes):
        self.type_ = type_
        self.attributes = attributes

    def __repr__(self):
        return "UonCustomType({}, {})".format(
            self.type_, self.attributes
        )

    def to_binary(self):
        return b"\x00"
