from uonrevisedtypes.scalars.uon_scalar import UonScalar


class UonBoolean(UonScalar):
    def __init__(self, value, presentation_properties={}):
        super().__init__(value, "bool", presentation_properties)

    def __repr__(self):
        return "UonBoolean({})".format(self.value)

    def __str__(self):
        return "!bool {}".format(self.value)

    def __bool__(self):
        """
        We override the built-in method __bool__ 
        to determine the truth value of UonBoolean, simply based
        on the boolean value it wraps.
        """
        return self.value

    def to_binary(self):
        return b"\x00"
