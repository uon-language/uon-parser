from uonrevisedtypes.scalars.uon_scalar import UonScalar


class UonNumeric(UonScalar):
    def __init__(self, value, uon_type, precision, unit=None,
                 presentation_properties={}):
        super().__init__(value, uon_type, presentation_properties)
        self.precision = precision
        self.unit = unit

    def __eq__(self, other):
        if isinstance(other, UonNumeric):
            return (self.value == other.value
                    and self.unit == other.unit)
        return NotImplemented

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return "{}({}, {!r})".format(
            self.__class__.__name__,
            self.value, self.unit)

    def __str__(self):
        num_to_string = f"!{self.uon_type} {self.value}"
        if self.unit is not None:
            num_to_string += f" {self.unit}"
        return num_to_string
