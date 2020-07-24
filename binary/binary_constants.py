UON_SEQ = b"\x01"
UON_MAPPING = b"\x02"
UON_STRING = b"\x11"
KEYNAME = b"\x12"
VALUE = b"\x13"
UON_BOOLEAN = b"\x14"
FLOAT = b"\x22"
FLOAT_32 = b"\x23"
FLOAT_64 = b"\x24"
FLOAT_128 = b"\x25"
INT = b"\x29"
INT_32 = b"\x33"
INT_64 = b"\x34"
INT_128 = b"\x35"
UINT = b"\x30"
"Uint32": \x39
"Uint64": \x3a
"Uint128": \x3b
"UonUrl": \x4c
"UonNull": \x10
"Schema": \x18
"TypeValidation": \x19
"ValidationProperty" (description: corresponds to !prop in the spec): \x0f
"PresentationProperty" (description: (a reserved type in the spec,
                           not attributed yet)): \x1e
"Validator" (description: (a reserved type in the spec,
                           not attributed yet)): \x1f
"min" (description: Keyword): \x07
"max" (description: Keyword): \x08
"num" (description: ("Does not exist as a UonType, 
                        Only there to denote numeric properties)): \x15
"description" (description: Keyword): \x04
"optional" (description: Keyword): \x05 
"true" (description: Keyword): \x01
"false" (description: Keyword): \x00
"kilogram" (description: unit Keyword): \x21
"gram" (description: unit Keyword): \x69
"meter" (description: unit Keyword): \x20
"kilometer" (description: unit Keyword): \x6a
"kelvin" (description: unit Keyword): \x24
"celsius" (description: unit Keyword): \x3c
"second" (description: unit Keyword): \x22
"minute" (description: unit Keyword): \x45
"EOL" (description: "Not like spec"): \x00
