from uonrevisedtypes.units.quantity import Quantity


class Mass(Quantity):
    pass


class Kilogram(Mass):
    def __str__(self):
        return "kg"

    def to_binary(self):
        pass


class Gram(Mass):
    def __str__(self):
        return "g"

    def to_binary(self):
        pass
