from abc import ABC, abstractmethod


class UonBase(ABC):
    def __init__(self):
        self.presentation_properties = {}

    @abstractmethod
    def to_binary(self):
        pass
