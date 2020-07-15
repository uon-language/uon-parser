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
from uonrevisedtypes.scalars.uon_string import UonString


def decode_binary(binary_input):
    return decode_binary_helper(binary_input, [])


def decode_binary_helper(binary_input, acc):
    if len(binary_input) == 0:
        return []
    elif binary_input.startswith(b"\x11"):
        # UonString
        return decode_string(binary_input[1:])
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
    pass


def decode_seq(binary_input):
    pass


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
    unpack_format = f"{length}s"
    value = struct.unpack(unpack_format, binary_input[2:])[0]
    return UonString(value.decode("utf-8"))


def decode_boolean(binary_input):
    if binary_input[0] == 0x00:
        return UonBoolean(False)
    elif binary_input[0] == 0x01:
        return UonBoolean(True)
    else:
        raise ValueError("Bad boolean value")


# TODO: Maybe inline these 3 functions
def decode_float(binary_input, precision):
    if precision == 32:
        return Float32(np.frombuffer(binary_input, dtype="float32"))
    elif precision == 64:
        return Float64(np.frombuffer(binary_input, dtype="float64"))
    elif precision == 128:
        return Float128(np.frombuffer(binary_input, dtype="float128"))
    else:
        raise ValueError("Bad Float value")


def decode_integer(binary_input, precision):
    if precision == 32:
        return Integer32(np.frombuffer(binary_input, dtype="int32"))
    elif precision == 64:
        return Integer64(np.frombuffer(binary_input, dtype="int64"))
    elif precision == 128:
        return Integer128(np.frombuffer(binary_input, dtype="int128"))
    else:
        raise ValueError("Bad Integer value")


def decode_uint(binary_input, precision):
    if precision == 32:
        return Uint32(np.frombuffer(binary_input, dtype="uint32"))
    elif precision == 64:
        return Uint64(np.frombuffer(binary_input, dtype="uint64"))
    elif precision == 128:
        return Uint128(np.frombuffer(binary_input, dtype="uint128"))
    else:
        raise ValueError("Bad Uint value")
