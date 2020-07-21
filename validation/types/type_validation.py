from abc import ABC, abstractmethod
from validation.validator import ValidationError


class ValidationType(ABC):

    @abstractmethod
    def validate_type(self, input_):
        """
        Given an input (a UON object), verifies the
        its type according to some validation.
        """
        pass

    @abstractmethod
    def to_binary(self):
        pass


class ValidationTypeError(ValidationError):
    def __init__(self, expression, message):
        super().__init__(expression, message)
