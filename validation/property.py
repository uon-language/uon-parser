from abc import ABC, abstractmethod
from validation.validator import ValidationError


class ValidationProperty(ABC):

    @abstractmethod
    def validate_property(self, input_):
        """
        Given an input (a UON object), verifies the
        validation property against it
        """
        pass


class ValidationPropertyError(ValidationError):
    def __init__(self, expression, message):
        super().__init__(expression, message)
