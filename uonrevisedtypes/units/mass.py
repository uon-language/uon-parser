from uonrevisedtypes.units.quantity import Quantity


class Mass(Quantity):
    pass


class Kilogram(Mass):
    def __str__(self):
        return "kg"

    def to_binary(self):
        return b"\x21"


class Gram(Mass):
    def __str__(self):
        return "g"

    def to_binary(self):
        return b"\x69"
