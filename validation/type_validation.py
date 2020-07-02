from abc import ABC, abstractmethod
from validation.validator import ValidationError


class ValidationType(ABC):

    @abstractmethod
    def validate_type(self, input_):
        """
        Given an input (a UON object), verifies the
        validation property against it
        """
        pass


class ValidationTypeError(ValidationError):
    def __init__(self, expression, message):
        super().__init__(expression, message)
