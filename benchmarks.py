import timeit

from uon_parser import UonParser
import numpy as np


data = """
{
    p: !!person {
        name: Stephane,
        age: !uint32 25,
        minor: !bool true
    },
    p2: !!person {
        name: Maggie Smith,
        age: !uint32 35,
        linkedin: !url www.maggie.smith@linkedin.com
    }
}
"""

schema_validation_2 = """
{p: !!person {
        name: Stephane, 
        age: !uint32 25,
        minor: !bool true,
        linkedin link: www.google.com,
        s: hole
    }
}
"""

schema_validation = """
{p: !!person {
        name: Stephane,
        age: !uint32 135,
        minor: !bool true
    }
}
"""

big_test_data = """
{p: !!person {
        name: Stephane,
        age: !uint32 135,
        minor: !bool true,
        description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
        sunt in culpa qui officia deserunt mollit anim id est laborum. "
    }
}
"""

p = UonParser()
"""encoded = p.to_binary(schema_validation)
decoded = p.from_binary(encoded)
print(decoded)
print(type(decoded))
print(str(decoded))
print(repr(decoded))
# Accessing UON attributes
user_type = decoded.value['p']
print(type(user_type))
print(str(user_type))
#p.load(str(decoded))"""

loaded_schema_validation = p.load(schema_validation)
print(loaded_schema_validation)

print()
print("========================================================================")
print()

print(p.load(schema_validation))
encoded = p.to_binary(schema_validation)
print(encoded)
decoded = p.from_binary(encoded)
print(decoded)
atr = decoded.value['p'].attributes.value['age']
print(type(atr.value))
print(atr)
print(type(atr))
print(repr(atr))

print()
print("========================================================================")
print()

schema = """
!!person: !schema {
    name (description: name of the person, optional: false): !str(min:3,
     max:25),
    age: !uint(min: 0, max: 125),
    minor (optional: false): !bool,
    linkedin link: !url
}
"""
schema_loaded = p.load(schema)
print(repr(schema_loaded))
#p.load(schema_validation)
