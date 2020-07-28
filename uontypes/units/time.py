from uontypes.units.quantity import Quantity


class Time(Quantity):
    pass


class Second(Time):
    def __str__(self):
        return "s"

    def to_binary(self):
        return b"\x22"


class Minute(Time):
    def __str__(self):
        return "min"

    def to_binary(self):
        return b"\x45"
