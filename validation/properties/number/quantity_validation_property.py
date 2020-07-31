from uontypes.scalars.uon_numeric import UonNumeric

from validation.properties.number.number_property_validation import (
    NumberPropertiesValidation
)

from validation.properties.property import ValidationPropertyError

from uontypes.units.length import Length
from uontypes.units.mass import Mass
from uontypes.units.temperature import Temperature
from uontypes.units.time import Time


class QuantityValidationProperty(NumberPropertiesValidation):
    def validate_property(self, input_):
        if not isinstance(input_, UonNumeric):
            raise ValueError("Quantity and unit validation"
                             " only apply to uon numeric types")

    def __repr__(self):
        return f"{self.__class__.__name__}()"


class LengthQuantityValidation(QuantityValidationProperty):
    def validate_property(self, input_):
        super().validate_property(input_)
        if not isinstance(input_.unit, Length):
            raise QuantityValidationError(f"Input quantity {input_.unit} does "
                                          "not correspond to "
                                          "length quantity.")

    def __str__(self):
        return "quantity: length"

    def to_binary(self):
        """Return the binary representation of a Length
        quantity validation instance.

        For Length, we return the byte representing the default unit
        for lengths, namely meters.

        Returns:
            bytes: byte encoding of LengthQuantityValidation
        """
        return b"\x20"


class MassQuantityValidation(QuantityValidationProperty):
    def validate_property(self, input_):
        super().validate_property(input_)
        if not isinstance(input_.unit, Mass):
            raise QuantityValidationError(f"Input quantity {input_.unit} does "
                                          "not correspond to "
                                          "mass quantity.")

    def __str__(self):
        return "quantity: mass"

    def to_binary(self):
        """Return the binary representation of a Mass
        quantity validation instance.

        For Mass, we return the byte representing the default unit
        for masses, namely kilograms.

        Returns:
            bytes: byte encoding of MassQuantityValidation
        """
        return b"\x21"


class TemperatureQuantityValidation(QuantityValidationProperty):
    def validate_property(self, input_):
        super().validate_property(input_)
        if not isinstance(input_.unit, Temperature):
            raise QuantityValidationError(f"Input quantity {input_.unit} does "
                                          "not correspond to "
                                          "temperature quantity.")

    def __str__(self):
        return "quantity: temperature"

    def to_binary(self):
        """Return the binary representation of a Temperature
        quantity validation instance.

        For Temperature, we return the byte representing the default unit
        for temperature, namely kelvins.

        Returns:
            bytes: byte encoding of TemperatureQuantityValidation
        """
        return b"\x24"


class TimeQuantityValidation(QuantityValidationProperty):
    def validate_property(self, input_):
        super().validate_property(input_)
        if not isinstance(input_.unit, Time):
            raise QuantityValidationError(f"Input quantity {input_.unit} does "
                                          "not correspond to "
                                          "time quantity.")

    def __str__(self):
        return "quantity: time"

    def to_binary(self):
        """Return the binary representation of a Time
        quantity validation instance.

        For Time, we return the byte representing the default unit
        for time, namely seconds.

        Returns:
            bytes: byte encoding of TimeQuantityValidation
        """
        return b"\x22"


class QuantityValidationError(ValidationPropertyError):
    pass
