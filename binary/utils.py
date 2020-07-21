import struct

EOL = b"\x00"

# Integer limit unsigned short
STRING_LENGTH_MAX_VALUE = 65535


def encode_string(input_string):
    """Encode the string value in binary using utf-8
    as well as its length (valuable info when decoding 
    later on). Length will be encoded as an unsigned
    short (max 65535).
    """
    input_string_encoded = input_string.encode("utf-8")
    length = len(input_string_encoded)
    length_encoded = struct.pack("<H", length)
    return length_encoded + input_string_encoded
