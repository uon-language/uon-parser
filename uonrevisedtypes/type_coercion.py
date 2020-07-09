from uonrevisedtypes.scalars.uon_float import Float32, Float64, Float128
from uonrevisedtypes.scalars.uon_integer import (
    Integer32, Integer64, Integer128
)
from uonrevisedtypes.scalars.uon_uint import (
    Uint32, Uint64, Uint128
)

from uonrevisedtypes.scalars.uon_string import UonString

type_constructors = {
    "float32": Float32,
    "float64": Float64,
    "float128": Float128,
    "int32": Integer32,
    "int64": Integer64,
    "int128": Integer128,
    "uint32": Uint32,
    "uint64": Uint64,
    "str": UonString
}