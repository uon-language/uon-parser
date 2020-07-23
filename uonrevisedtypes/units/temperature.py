from uonrevisedtypes.units.quantity import Quantity


class Temperature(Quantity):
    pass


class Kelvin(Temperature):
    def __str__(self):
        return "K"

    def __repr__(self):
        return "Kelvin()"

    def to_binary(self):
        pass


class Celsius(Temperature):
    def __str__(self):
        return "C"

    def __repr__(self):
        return "Celsius()"

    def to_binary(self):
        pass
