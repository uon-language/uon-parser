import struct

from validation.schema import Schema
from validation.validator import Validator

from validation.types.number.uint_type_validation import UintTypeValidation

from validation.properties.number.number_max_property import MaxNumberValidation
from validation.properties.number.number_min_property import MinNumberValidation

from binary.utils import EOL, encode_string


# We use < for little-endian.
float32_struct = struct.Struct("<f")
float64_struct = struct.Struct("<d")
int32_struct = struct.Struct("<i")
int64_struct = struct.Struct("<q")
uint32_struct = struct.Struct("<I")
uint64_struct = struct.Struct("<Q")
char_struct = struct.Struct("<b")


# ============================== ENCODING ==============================
class TestValidatorToBinary:

    def test_simple_validator_to_binary(self):
        v = Validator(UintTypeValidation(),
                      [MinNumberValidation(0.0), MaxNumberValidation(125.0)],
                      {"description": "An unsigned integer validator"})
        
        assert (b"\x1f\x19\x30\x0f\x15\x07" + struct.pack("<d", 0)
                + b"\x0f\x15\x08" + struct.pack("<d", 125)
                + b"\x1e" + b"\x04" + encode_string("An unsigned integer"
                                                    " validator")
                + EOL) == v.to_binary()


class TestSchemaToBinary:
    def test_simple_schema_to_binary(self):
        v = Validator(UintTypeValidation(),
                      [MinNumberValidation(0.0), MaxNumberValidation(125.0)],
                      {"description": "An unsigned integer validator"})
        
        s = Schema("person", {"age": v}, name="person", 
                   description="a person schema")
        
        assert (b"\x18" + encode_string("person")
                + encode_string("person")
                + encode_string("a person schema")
                + EOL
                + b"\x12" + encode_string("age")
                + v.to_binary()
                + EOL) == s.to_binary()
        