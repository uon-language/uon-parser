import numpy as np
import struct

from uonrevisedtypes.scalars.uon_bool import UonBoolean
from uonrevisedtypes.scalars.uon_float import (
    Float32, Float64, Float128
)
from uonrevisedtypes.scalars.uon_integer import (
    Integer32, Integer64, Integer128
)
from uonrevisedtypes.scalars.uon_uint import (
    Uint32, Uint64, Uint128
)
from uonrevisedtypes.scalars.uon_url import UonUrl
from uonrevisedtypes.uon_null import UonNull
from uonrevisedtypes.scalars.uon_string import UonString
from uonrevisedtypes.collections.uon_dict import UonMapping
from uonrevisedtypes.collections.uon_seq import UonSeq

from uonrevisedtypes.units.length import (
    Length, Kilometer, Meter
)

from uonrevisedtypes.units.mass import (
    Mass, Kilogram, Gram
)

from uonrevisedtypes.units.temperature import (
    Temperature, Kelvin, Celsius
)

from uonrevisedtypes.units.time import (
    Time, Second, Minute
)

from validation.schema import Schema
from validation.validator import Validator
from validation.properties.number.number_max_property import (
    MaxNumberValidation
)
from validation.properties.number.number_min_property import (
    MinNumberValidation
)
from validation.properties.string.string_max_property import (
    MaxStringValidation
)
from validation.properties.string.string_min_property import (
    MinStringValidation
)

from validation.properties.number.quantity_validation_property import (
    LengthQuantityValidation, MassQuantityValidation,
    TemperatureQuantityValidation, TimeQuantityValidation
)

from validation.types.string.string_type_validation import StringTypeValidation
from validation.types.number.int_type_validation import IntegerTypeValidation
from validation.types.number.float_type_validation import FloatTypeValidation
from validation.types.number.uint_type_validation import UintTypeValidation
from validation.types.boolean.bool_type_validation import BooleanTypeValidation
from validation.types.url.url_type_validation import UrlTypeValidation

from binary.utils import decode_number
import binary.binary_constants as binary_constants

import logging
logging.basicConfig(level=logging.DEBUG)


"""Dictionary of all Uon numeric scalar constructors and
their corresponding numpy dtype"""
NUMERIC_SCALAR_CONSTRUCTORS = {
    "int32": Integer32,
    "int64": Integer64,
    "int128": Integer128,
    "float32": Float32,
    "float64": Float64,
    "float128": Float128,
    "uint32": Uint32,
    "uint64": Uint64,
    "uint128": Uint128
}

DEFAULT_QUANTITY_BINARY = {
    0x21: Mass,
    0x20: Length,
    0x22: Time,
    0x24: Temperature
}

QUANTITY_UNIT_BINARY = {
    0x21: Kilogram,
    0x69: Gram,
    0x20: Meter,
    0x6a: Kilometer,
    0x24: Kelvin, 
    0x3c: Celsius,
    0x22: Second,
    0x45: Minute
}

TYPE_VALIDATIONS = {
    0x4c: UrlTypeValidation,
    0x11: StringTypeValidation,
    0x14: BooleanTypeValidation,
    0x22: FloatTypeValidation,
    0x29: IntegerTypeValidation,
    0x30: UintTypeValidation
}

PRECISIONS = [32, 64, 128]


class UonBinaryDecodingError(Exception):
    pass


def decode_binary(binary_input):
    if len(binary_input) == 0:
        raise UonBinaryDecodingError("Empty Binary")
    elif binary_input.startswith(b"\x01"):
        return decode_seq(binary_input[1:])[0]
    elif binary_input.startswith(b"\x02"):
        return decode_mapping(binary_input[1:])[0]
    else:
        raise UonBinaryDecodingError("Bad Binary")


def decode_binary_value(binary_input):
    if len(binary_input) == 0:
        raise UonBinaryDecodingError("Empty Binary Value")
    elif binary_input.startswith(b"\x10"):
        # UonNull (no value to decode)
        return UonNull(), binary_input[1:]
    elif binary_input.startswith(b"\x4c"):
        # UonUrl
        return decode_uon_url(binary_input[1:])
    elif binary_input.startswith(b"\x11"):
        # UonString
        return decode_uon_string(binary_input[1:])
    elif binary_input.startswith(b"\x14"):
        # UonBoolean
        return decode_boolean(binary_input[1:])
    elif binary_input.startswith(b"\x23"):
        # Float32
        return decode_float(binary_input[1:], 32)
    elif binary_input.startswith(b"\x24"):
        # Float64
        return decode_float(binary_input[1:], 64)
    elif binary_input.startswith(b"\x25"):
        # Float128
        return decode_float(binary_input[1:], 128)
    elif binary_input.startswith(b"\x33"):
        # Integer32
        return decode_integer(binary_input[1:], 32)
    elif binary_input.startswith(b"\x34"):
        # Integer64
        return decode_integer(binary_input[1:], 64)
    elif binary_input.startswith(b"\x35"):
        # Integer128
        return decode_integer(binary_input[1:], 128)
    elif binary_input.startswith(b"\x39"):
        # Uint32
        return decode_uint(binary_input[1:], 32)
    elif binary_input.startswith(b"\x3a"):
        # Uint64
        return decode_uint(binary_input[1:], 64)
    elif binary_input.startswith(b"\x3b"):
        # Uint128
        return decode_uint(binary_input[1:], 128)
    elif binary_input.startswith(b"\x01"):
        # UonSeq
        return decode_seq(binary_input[1:])
    elif binary_input.startswith(b"\x02"):
        # UonMapping
        return decode_mapping(binary_input[1:])
    else:
        raise UonBinaryDecodingError("Undefined binary")


def decode_mapping(binary_input):
    retval = {}
    rest = binary_input
    while rest.startswith(b"\x12"):
        key, value_encoded = decode_string(rest[1:])
        value, rest = decode_binary_value(value_encoded)
        retval[key] = value
    # Return rest[1:] to get rid of the final EOL byte
    return UonMapping(retval), rest[1:]


def decode_seq(binary_input):
    retval = []
    rest = binary_input
    while not rest.startswith(b"\x00"):
        value, rest = decode_binary_value(rest)
        retval.append(value)
    # Return rest[1:] to get rid of the final EOL byte
    return UonSeq(retval), rest[1:]


def decode_uon_url(binary_input):
    decoded_string, rest = decode_string(binary_input)
    return UonUrl(decoded_string), rest


def decode_uon_string(binary_input):
    decoded_string, rest = decode_string(binary_input)
    return UonString(decoded_string), rest


def decode_string(binary_input):
    """Decode a binary uon string. Length of the string is encoded 
    on the two first bytes, the string value is utf-8 encoded on the rest.

    Args:
        binary_input (bytes): a binary uon string

    Returns:
        tuple: uon string with the decoded value, 
                and the rest of the binary
    """
    length_encoded = binary_input[0:2]
    length = struct.unpack("<H", length_encoded)[0]
    end_string_offset = length + 2

    encoded_value = binary_input[2:end_string_offset]
    rest = binary_input[end_string_offset:]

    unpack_format = f"{length}s"
    value = struct.unpack(unpack_format, encoded_value)[0]
    return value.decode("utf-8"), rest


def decode_boolean(binary_input):
    rest = binary_input[1:]
    value: UonBoolean
    if binary_input[0] == 0x00:
        value = UonBoolean(False)
    elif binary_input[0] == 0x01:
        value = UonBoolean(True)
    else:
        raise UonBinaryDecodingError("Bad boolean value")
    return value, rest


def decode_float(binary_input, precision):
    if precision not in PRECISIONS:
        raise UonBinaryDecodingError("Bad Float value")
    return decode_numeric_scalar(binary_input, "float", precision)


def decode_integer(binary_input, precision):
    if precision not in PRECISIONS:
        raise UonBinaryDecodingError("Bad Integer value")
    return decode_numeric_scalar(binary_input, "int", precision)


def decode_uint(binary_input, precision):
    if precision not in PRECISIONS:
        raise UonBinaryDecodingError("Bad Uint value")
    return decode_numeric_scalar(binary_input, "uint", precision)


def decode_numeric_scalar(binary_input, numpy_dtype, precision):
    """Given a binary input, a numpy data type and the precision,
    Reconstruct the UonNumeric value.

    The datatype (float, int...) is prepended
    to the precision to get the numpy datatype.
    That datatype is used to reconstruct the numpy value using
    np.frombuffer, and finally the UonNumericValue.

    The last byte of a UonNumeric represents the encoded quantity unit
    if there is one. If there is None, the byte will be \x00.

    Args:
        binary_input (bytes): the binary input representing a UonNumeric
        numpy_dtype (str): the datatype
        precision (int): the precision

    Returns:
        UonNumeric: The decoded UonNumeric instance.
    """
    numpy_dtype = numpy_dtype + str(precision)
    encoded_value, rest = split_nb_bytes(binary_input, precision)
    numpy_decoded_value = np.frombuffer(encoded_value, dtype=numpy_dtype)

    unit_encoded, rest = rest[0], rest[1:]
    unit_decoded = decode_unit(unit_encoded)

    retval = NUMERIC_SCALAR_CONSTRUCTORS[numpy_dtype](numpy_decoded_value,
                                                      unit=unit_decoded)

    return retval, rest


def split_nb_bytes(binary_input, precision):
    """Given a binary input and a precision,
    calculates the number of bytes necessary to encode a number with said
    precision. It then uses this to split the binary input and return a tuple
    with the first element containing the binary string encoded number,
    and the second element containing the rest of the binary input.

    Args:
        binary_input (bytes): the binary_input that starts with an encoded
                                UonNumeric.
        precision (int): precision of the encoded number

    Returns:
        tuple: a tuple with the first element the encoded number
                and the second element is the rest of the binary
    """
    number_of_bytes = int(precision/8)
    return binary_input[:number_of_bytes], binary_input[number_of_bytes:]


def decode_unit(binary_input):
    """Decode the quantity unit in a UonNumeric binary.

    The quantity is encoded on a single byte (at the end of a binary
    UonNumeric). if it is 0x00, then this means that there is no
    unit.

    Args:
        binary_input (bytes): the single-byte encoded quantity

    Returns:
        Quantity: The decoded quantity unit
    """
    if binary_input == 0x00:
        return None
    unit_decoded = QUANTITY_UNIT_BINARY.get(binary_input)()
    if unit_decoded is None:
        raise UonBinaryDecodingError("Bad binary for quantity unit")
    return unit_decoded


# ============================== SCHEMA DECODING ==============================
def decode_presentation_properties(binary_input):
    presentation_properties = {}
    # Consume the \x1e byte that marks the presentation properties
    rest = binary_input[1:]

    # Decode description if there is one
    if rest.startswith(b"\x04"):
        description, rest = decode_string(rest[1:])
        presentation_properties["description"] = description

    if rest.startswith(b"\x05"):
        # optional property is stored as a UonBoolean instance
        optional, rest = decode_boolean(rest[1:])
        presentation_properties["optional"] = optional

    return presentation_properties, rest


def decode_validation_property(binary_input):
    property_encoded_start, rest = binary_input[0], binary_input[1:]
    if property_encoded_start == 0x11:
        # String validation properties
        if rest.startswith(b"\x08"):
            decoded_max, rest = decode_number(rest[1:], "uint16")
            return MaxStringValidation(decoded_max), rest
        elif rest.startswith(b"\x07"):
            decoded_min, rest = decode_number(rest[1:], "uint16")
            return MinStringValidation(decoded_min), rest
    if property_encoded_start == 0x15:
        # Number validation properties
        if rest.startswith(b"\x08"):
            decoded_max, rest = decode_number(rest[1:], "float64")
            return MaxNumberValidation(decoded_max), rest
        elif rest.startswith(b"\x07"):
            decoded_min, rest = decode_number(rest[1:], "float64")
            return MinNumberValidation(decoded_min), rest
    if property_encoded_start == binary_constants.KILOGRAM:
        return MassQuantityValidation(), rest
    if property_encoded_start == binary_constants.METER:
        return LengthQuantityValidation(), rest
    if property_encoded_start == binary_constants.SECOND:
        return TimeQuantityValidation(), rest
    if property_encoded_start == binary_constants.KELVIN:
        return TemperatureQuantityValidation(), rest
    raise UonBinaryDecodingError("Unknown Validation Property")


def decode_validation_type(binary_input):
    type_validation_encoded, rest = binary_input[0], binary_input[1:]
    type_validation = TYPE_VALIDATIONS.get(type_validation_encoded)()
    if type_validation is None:
        raise UonBinaryDecodingError("Unknown Type Validation")
    return type_validation, rest


def decode_validator(binary_input):
    # Consume the initial \x1f byte that marks a validator
    # as well as the following obligatory \x19 byte that marks
    # a type validation
    rest = binary_input[2:]
    type_validation, rest = decode_validation_type(rest)

    # Decode the list of validation properties
    validation_properties = []
    while rest.startswith(b"\x0f"):
        validation_property, rest = decode_validation_property(rest[1:])
        validation_properties.append(validation_property)
    
    # Next, decode the presentation properties that a validator validates
    presentation_properties = {}
    if rest[0] == 0x1e:
        presentation_properties, rest = decode_presentation_properties(rest)

    v = Validator(type_validation, 
                  properties_validations=validation_properties,
                  presentation_properties=presentation_properties)
    return v, rest


def decode_schema(binary_input):
    # Consume the \x18 byte that marks a schema
    rest = binary_input[1:]

    # Get the type which is an encoded string
    type_, rest = decode_string(rest)

    # Decode the schema presentation properties
    schema_name, rest = decode_schema_presentation_property(
        rest, decode_string
    )
    schema_description, rest = decode_schema_presentation_property(
        rest, decode_string
    )
    # For schema uuid, we're dealing with an encoded UonUrl,
    # so we need to consume the characteristic \x4c byte
    schema_uuid, rest = decode_schema_presentation_property(
        rest[1:], decode_uon_url
    )

    # Decode validators
    validators = {}
    while rest.startswith(b"\x12"):
        attribute, validator_encoded = decode_string(rest[1:])
        validator, rest = decode_validator(validator_encoded)
        validators[attribute] = validator

    schema = Schema(type_, validators=validators,
                    name=schema_name, description=schema_description,
                    uuid=schema_uuid)
    # Return rest[1:] to get rid of the final EOL byte
    return schema, rest[1:]


def decode_schema_presentation_property(binary_input, decode_function):
    p = None
    encoded_property_start, rest = binary_input[0], binary_input[1:]
    if not encoded_property_start == 0x00:
        p, rest = decode_function(binary_input)
    return p, rest
