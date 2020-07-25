from uon import Uon

from binary.utils import encode_string

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

    def to_binary(self):
        """Return binary representation of a uon user type.

        The characteristic byte of a uon user type is 0x1a.

        Returns:
            bytes: binary representation of a uon user type
        """
        return (b"\x1a"
                + encode_string(self.type_)
                + self.attributes.to_binary())
