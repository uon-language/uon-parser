import struct

from uonrevisedtypes.scalars.uon_bool import UonBoolean
from uonrevisedtypes.scalars.uon_float import (
    Float32, Float64, Float128
)
from uonrevisedtypes.scalars.uon_uint import (
    Uint32, Uint64, Uint128
)
from uonrevisedtypes.scalars.uon_integer import (
    Integer32, Integer64
)
from uonrevisedtypes.scalars.uon_string import UonString

from uonrevisedtypes.collections.uon_dict import UonMapping
from uonrevisedtypes.collections.uon_seq import UonSeq

from uonrevisedtypes.uon_custom_type import UonCustomType

from uonrevisedtypes.units.length import Meter
from uonrevisedtypes.units.mass import Kilogram

from binary.codec import (
    decode_binary,
    decode_binary_value,
    decode_float,
    decode_integer,
    decode_uint,
    decode_boolean,
    decode_string
)
from binary.utils import encode_string, EOL

# We use < for little-endian since numpy is used to represent
# numbers in uon-parser and numpy byte encoding is little-endian.
float32_struct = struct.Struct("<f")
float64_struct = struct.Struct("<d")
int32_struct = struct.Struct("<i")
int64_struct = struct.Struct("<q")
uint32_struct = struct.Struct("<I")
uint64_struct = struct.Struct("<Q")
char_struct = struct.Struct("<b")

# ============================== ENCODING ==============================


class TestUonEncoding:
    def test_bool_to_binary(self):
        b = UonBoolean(True)
        assert b.to_binary() == b"\x14\x01"
        b = UonBoolean(False)
        assert b.to_binary() == b"\x14\x00"

    def test_float_to_binary(self):
        test_value = 64.0
        f = Float64(test_value)
        assert f.to_binary() == (b"\x24"
                                 + float64_struct.pack(test_value)
                                 + b"\x00")
        f = Float32(test_value)
        assert f.to_binary() == (b"\x23"
                                 + float32_struct.pack(test_value)
                                 + b"\x00")

    def test_uint_to_binary(self):
        test_value = 64
        f = Uint64(test_value)
        assert f.to_binary() == (b"\x3a"
                                 + uint64_struct.pack(test_value)
                                 + b"\x00")
        f = Uint32(test_value)
        assert f.to_binary() == (b"\x39"
                                 + uint32_struct.pack(test_value)
                                 + b"\x00")

    def test_num_quantity_to_binary(self):
        test_value = 64
        f = Integer32(test_value, unit=Meter())
        assert f.to_binary() == (
            b"\x33" + int32_struct.pack(test_value)
            + b"\x20"
        )
        f = Integer64(test_value, unit=Kilogram())
        assert f.to_binary() == (
            b"\x34" + int64_struct.pack(test_value)
            + b"\x21"
        )

    def test_string_to_binary(self):
        test_value = "Hello, world!"
        test_value_encoded = b"\x48\x65\x6c\x6c\x6f\x2c\x20\x77\x6f\x72\x6c\x64\x21"
        length_encoded = struct.pack("<H", len(test_value))
        test_value_binary = b"\x11" + length_encoded + test_value_encoded
        s = UonString(test_value)
        assert s.to_binary() == test_value_binary

    def test_uon_user_type(self):
        attributes = {"name": UonString("John"), "age": Uint32(187)}
        test_value = UonCustomType("person", UonMapping(attributes))
        assert (b"\x1a"
                + encode_string("person")
                + b"\x02" + b"\x12" + encode_string("name") + b"\x11"
                + encode_string("John")
                + b"\x12" + encode_string("age") + b"\x39"
                + uint32_struct.pack(187) + 2 * EOL
                == test_value.to_binary())
# ============================== DECODING ==============================


class TestUonDecoding:
    def test_binary_to_bool(self):
        assert decode_binary_value(b"\x14\x01")[0] == UonBoolean(True)
        assert decode_binary_value(b"\x14\x00")[0] == UonBoolean(False)

    def test_binary_to_float(self):
        test_value = b"\x24\x00\x00\x00\x00\x00\x00i@\x00"
        assert decode_binary_value(test_value)[0] == Float64(200.0)
        test_value = b"\x23\x00\x00HC\x00"
        assert decode_binary_value(test_value)[0] == Float32(200.0)

    def test_binary_to_uint(self):
        test_value = b"\x3a\xc8\x00\x00\x00\x00\x00\x00\x00\x00"
        assert decode_binary_value(test_value)[0] == Uint64(200)
        test_value = b"\x39\xc8\x00\x00\x00\x00"
        assert decode_binary_value(test_value)[0] == Uint32(200)

    def test_binary_to_num_quantity(self):
        test_value = b"\x24\x00\x00\x00\x00\x00\x00i@\x21"
        assert (
            decode_binary_value(test_value)[0]
            ==
            Float64(200.0, unit=Kilogram())
        )

    def test_binary_to_string(self):
        test_value = b"\x11\r\x00Hello, world!"
        assert decode_binary_value(test_value)[0] == UonString("Hello, world!")

    def test_binary_to_dict(self):
        test_value = b"\x02\x12\x05\x00happy\x11\x03\x00yes\x12\x03\x00sad\x11\x02\x00no\x00"
        assert (decode_binary(test_value)
                ==
                UonMapping({"happy": UonString("yes"),
                            "sad": UonString("no")}))
