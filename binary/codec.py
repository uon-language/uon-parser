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

PRECISIONS = [32, 64, 128]


def decode_binary(binary_input):
    if len(binary_input) == 0:
        raise ValueError("Empty Binary")
    elif binary_input.startswith(b"\x01"):
        return decode_seq(binary_input[1:])[0]
    elif binary_input.startswith(b"\x02"):
        return decode_mapping(binary_input[1:])[0]
    else:
        raise ValueError("Bad Binary")


def decode_binary_value(binary_input):
    if len(binary_input) == 0:
        raise ValueError("Empty Binary Value")
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
        raise ValueError("Undefined binary")


def decode_mapping(binary_input):
    retval = {}
    rest = binary_input
    while rest.startswith(b"\x12"):
        key, value_encoded = decode_string(rest[1:])
        value, rest = decode_binary_value(value_encoded)
        retval[key] = value
    # Return rest[1:] to get rid of the initial EOL byte
    return UonMapping(retval), rest[1:]


def decode_seq(binary_input):
    retval = []
    rest = binary_input
    while not rest.startswith(b"\x00"):
        value, rest = decode_binary_value(rest)
        retval.append(value)
    # Return rest[1:] to get rid of the initial EOL byte
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
        UonString: uon string with the decoded value
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
        raise ValueError("Bad boolean value")
    return value, rest


def decode_float(binary_input, precision):
    if precision not in PRECISIONS:
        raise ValueError("Bad Float value")
    return decode_numeric_scalar(binary_input, "float", precision)


def decode_integer(binary_input, precision):
    if precision not in PRECISIONS:
        raise ValueError("Bad Integer value")
    return decode_numeric_scalar(binary_input, "int", precision)


def decode_uint(binary_input, precision):
    if precision not in PRECISIONS:
        raise ValueError("Bad Uint value")
    return decode_numeric_scalar(binary_input, "uint", precision)


def decode_numeric_scalar(binary_input, numpy_dtype, precision):
    numpy_dtype = numpy_dtype + str(precision)
    encoded_value, rest = split_nb_bytes(binary_input, precision)
    numpy_decoded_value = np.frombuffer(encoded_value, dtype=numpy_dtype)
    retval = NUMERIC_SCALAR_CONSTRUCTORS[numpy_dtype](numpy_decoded_value)
    return retval, rest


def split_nb_bytes(binary_input, precision):
    number_of_bytes = int(precision/8)
    return binary_input[:number_of_bytes], binary_input[number_of_bytes:]


# ============================== SCHEMA DECODING ==============================
def decode_presentation_properties(binary_input):
    return {}

def decode_validation_property(binary_input):
    return ""

def decode_validation_type(binary_input):
    return ""

def decode_validator(binary_input):
    return ""

def decode_validators(binary_input):
    return {}

def decode_schema(binary_input):
    return ""
