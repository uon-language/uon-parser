import timeit
import sys

from uon_parser import UonParser, validate

schema = """
!!person: !schema {
    name (description: name of the person, optional: false): !str(min:3,
     max:25),
    age: !uint(min: 0, max: 125),
    minor (optional: false): !bool,
    linkedin link: !url
}
"""

data = """
{
    p: !!person {
        name: Stephane,
        age: !uint32 25,
        minor: !bool false
    },
    p2: !!person {
        name: Maggie Smith,
        age: !uint32 35,
        minor: !bool false,
        linkedin: !url www.maggie.smith@linkedin.com
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


validate("""
{
    p: !!person {
        name: Stephane,
        age: !uint32 25,
        minor: !bool false
    },
    p2: !!person {
        name: Maggie Smith,
        age: !uint32 35,
        minor: !bool false,
        linkedin: !url www.maggie.smith@linkedin.com
    }
}
""", schema_raw=schema)

p = UonParser()
loaded = p.load_from_file("benchmarks.uon")
print(loaded)

binary = p.to_binary(data)
print(binary)
print(sys.getsizeof(binary))
decoded = p.from_binary(binary)
print(decoded)
print(str(decoded) == str(loaded))

mysetup_data = '''from uon_parser import UonParser
'''
s = '''
p = UonParser()
p.load_from_file("benchmarks.uon")
'''

#print("loading UON time: ", timeit.timeit(setup=mysetup_data, stmt=s, number=100))
