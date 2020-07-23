from abc import ABC, abstractmethod


class Uon(ABC):
    """Definition of Uon Type.

    Defines one essential method to_binary that each deriving Uon type has 
    to implement, which is the uon binary representation of that type.
    """
    @abstractmethod
    def to_binary():
        pass