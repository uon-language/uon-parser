from uontypes.scalars.uon_float import Float32, Float64, Float128
from uontypes.scalars.uon_integer import (
    Integer32, Integer64, Integer128
)
from uontypes.scalars.uon_uint import (
    Uint32, Uint64, Uint128
)

type_constructors = {
    "float": Float64,
    "float32": Float32,
    "float64": Float64,
    "float128": Float128,
    "int": Integer64,
    "int32": Integer32,
    "int64": Integer64,
    "int128": Integer128,
    "uint": Uint64,
    "uint32": Uint32,
    "uint64": Uint64
}