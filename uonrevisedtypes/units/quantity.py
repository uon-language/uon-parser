from uon import Uon


class Quantity(Uon):
    """Represents a physical quantity in Uon.

    A quantity is expressed in units.
    """
    def __repr__(self):
        return f"{self.__class__.__name__}()"
