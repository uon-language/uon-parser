import pprint

from uon import Uon
from binary.utils import EOL, encode_presentation_properties


class Validator(Uon):
    def __init__(self, type_validation, properties_validations=[],
                 presentation_properties={}):
        if properties_validations is None:
            properties_validations = []
        if presentation_properties is None:
            presentation_properties = {}
        self.type_validation = type_validation
        self.properties_validations = properties_validations
        self.presentation_properties = presentation_properties

    def validate(self, input_):
        self.type_validation.validate_type(input_)
        for property_validation in self.properties_validations:
            property_validation.validate_property(input_)

    def __repr__(self):
        return "Validator({!r}, {}, {})".format(
            self.type_validation, pprint.pformat(self.properties_validations),
            self.presentation_properties)

    def __str__(self):
        properties_to_string = map(lambda x: str(x),
                                   self.properties_validations)
        return (f'{str(self.type_validation)} '
                f'({", ".join(properties_to_string)})')

    def to_binary(self):
        """Return the binary string representation
        of a validator. A validator always has a type validation, 
        an optional number of validation properties, and an optional number 
        of presentation properties.

        Returns:
            bytes: the binary string representation of a validator
        """
        validation_properties_to_binary = b""
        for p in self.properties_validations:
            validation_properties_to_binary += b"\x0f" + p.to_binary()

        presentation_properties_to_binary = encode_presentation_properties(
            self.presentation_properties
        )

        return (b"\x1f" + b"\x19" + self.type_validation.to_binary()
                + validation_properties_to_binary
                + presentation_properties_to_binary
                + EOL)


class ValidationError(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
