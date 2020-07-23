from uon import Uon


class UonCustomType(Uon):
    """
    A class to represent a user-defined type in UON.
    """
    def __init__(self, type_, attributes):
        """
        Parameters
        ----------
        type_: str
               the name of the user type
        attributes: UonMapping
                    attributes of the object of that type
        """
        self.type_ = type_
        self.attributes = attributes

    def __repr__(self):
        return "UonCustomType({}, {})".format(
            self.type_, self.attributes
        )
    
    def __str__(self):
        return f"!!{self.type_} {self.attributes}"

    # TODO
    def to_binary(self):
        return b"\x00"
