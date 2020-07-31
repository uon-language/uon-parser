from uontypes.uon_value import UonValue


class UonNull(UonValue):
    def __init__(self, presentation_properties={}):
        super().__init__(None, "null", presentation_properties)

    def __str__(self):
        return "null"

    def __repr__(self):
        return "UonNull()"

    def __eq__(self, other):
        """Override equals method. If the other instance
        is UonNull then by default return true, since there
        is no value to compare.

        Args:
            other (UonNull): Value to compare to.

        Returns:
            bool: Result of equals
        """
        if isinstance(other, UonNull):
            return True
        return NotImplemented

    def to_binary(self):
        return b"\x10"
