from uon import Uon


class Quantity(Uon):
    """Represents a physical quantity in Uon.

    A quantity is expressed in units.
    """
    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def __eq__(self, other):
        """ Implement equivalence equality for quantities.

        Since quantities and units don't have any attributes,
        we only need to check if the types match.
        """
        return type(other) is type(self)
