from uonrevisedtypes.units.quantity import Quantity


class Time(Quantity):
    pass


class Second(Time):
    def __str__(self):
        return "s"

    def __repr__(self):
        return "Second()"

    def to_binary(self):
        pass


class Minute(Time):
    def __str__(self):
        return "min"

    def __repr__(self):
        return "Minute()"

    def to_binary(self):
        pass
