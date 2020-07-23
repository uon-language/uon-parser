from uonrevisedtypes.units.quantity import Quantity


class Length(Quantity):
    pass


class Kilometer(Length):
    def __str__(self):
        return "km"

    def __repr__(self):
        return "Kilometer()"

    def to_binary(self):
        pass


class Meter(Length):
    def __str__(self):
        return "m"

    def __repr__(self):
        return "Meter()"

    def to_binary(self):
        pass