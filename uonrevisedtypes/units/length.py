from uonrevisedtypes.units.quantity import Quantity


class Length(Quantity):
    pass


class Kilometer(Length):
    def __str__(self):
        return "km"

    def to_binary(self):
        pass


class Meter(Length):
    def __str__(self):
        return "m"

    def to_binary(self):
        pass