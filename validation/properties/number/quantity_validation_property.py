from uonrevisedtypes.scalars.uon_numeric import UonNumeric

from validation.properties.number.number_property_validation import (
    NumberPropertiesValidation
)

from uonrevisedtypes.units.length import Length
from uonrevisedtypes.units.mass import Mass
from uonrevisedtypes.units.temperature import Temperature
from uonrevisedtypes.units.time import Time


class QuantityValidationProperty(NumberPropertiesValidation):
    def validate_property(self, input_):
        if not isinstance(input_, UonNumeric):
            raise ValueError("Quantity and unit validation"
                             " only apply to uon numeric types")

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def to_binary(self):
        return b"\x00"


class LengthQuantityValidation(QuantityValidationProperty):
    def validate_property(self, input_):
        super().validate_property(input_)
        if not isinstance(input_.unit, Length):
            raise QuantityValidationError(f"Input quantity {input_.unit} does "
                                          "not correspond to "
                                          "length quantity.")

    def __str__(self):
        return "quantity: length"


class MassQuantityValidation(QuantityValidationProperty):
    def validate_property(self, input_):
        super().validate_property(input_)
        if not isinstance(input_.unit, Mass):
            raise QuantityValidationError(f"Input quantity {input_.unit} does "
                                          "not correspond to "
                                          "mass quantity.")

    def __str__(self):
        return "quantity: mass"


class TemperatureQuantityValidation(QuantityValidationProperty):
    def validate_property(self, input_):
        super().validate_property(input_)
        if not isinstance(input_.unit, Temperature):
            raise QuantityValidationError(f"Input quantity {input_.unit} does "
                                          "not correspond to "
                                          "temperature quantity.")

    def __str__(self):
        return "quantity: temperature"


class TimeQuantityValidation(QuantityValidationProperty):
    def validate_property(self, input_):
        super().validate_property(input_)
        if not isinstance(input_.unit, Time):
            raise QuantityValidationError(f"Input quantity {input_.unit} does "
                                          "not correspond to "
                                          "time quantity.")

    def __str__(self):
        return "quantity: time"


class QuantityValidationError(Exception):
    pass
