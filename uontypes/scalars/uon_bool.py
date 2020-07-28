from uontypes.scalars.uon_scalar import UonScalar


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

    def __eq__(self, other):
        """Overrides the default implementation
        Overriding __ne__ is unnecessary since Python3.
        By default, __ne__() delegates to __eq__() and 
        inverts the result unless it is NotImplemented.
        Check https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
        """
        if isinstance(other, UonBoolean):
            return self.value == other.value
        return NotImplemented

    def __hash__(self):
        """Have to implement hash since overriding equals
        make the type unhashable.
        """
        return hash(self.value)

    def to_binary(self):
        return b"\x14" + (b"\x01" if self.value else b"\x00")
