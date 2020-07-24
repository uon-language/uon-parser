from pathlib import Path
from lark import Lark
from pprint import pprint

from transformer.uon_2_revised_tree_transformer import (
    UON2RevisedTreeToPython,
    TreeIndenter
)

from binary.codec import decode_binary, decode_binary_value

# import struct

# from validation.validator import Validator

# from validation.types.number.uint_type_validation import UintTypeValidation

# from validation.properties.number.number_max_property import MaxNumberValidation
# from validation.properties.number.number_min_property import MinNumberValidation

import logging
logging.basicConfig(level=logging.DEBUG)

uon_2_grammar_file = Path('grammar/uon_2_revised_grammar.lark')

simple_mapping_example = """
happy: yes
scale: null
"""

simple_seq_example = """
- happy
- sad
"""

simple_nested_mapping_example = """
happy: yes
scale: 
    max: 10
    min: 0
"""

simple_nested_seq_example = """
- a
- 
    - b
    - c
"""

test_multiline_string_json = """
{
    a: an example of a loooong
    string, b: (Another example of 
    a loooooooooong string)
}
"""

test_multiline_string_yaml = """
a : a normal string
b : (32000000 is a very loooooooooooooooong
number)
"""

test_true_false = """
old: !bool false
young(optional : false): true
oldAgain: true
"""

test_json = """
{foo : 42,
bar: {
    hey: ho,
    boy: hood
},
l : [one, 2, three]}
"""

test_uon_simple = """
foo (description: "A foo", optional: true): 42
h : 1
"""

test_uon = """
foo (description: "A foo", optional: true): 42
nested (description: "A dictionary"):
    h: 1
    c: 2
"""

test_number_coercion = """
foo: !uint32 123 km
bar: !float !int 65
"""

test_schema = """
!!person: !schema {
    name(description: name of the person, optional: false): !str(min:3, max:25),
    age: !uint(min: 0, max: 125),
    minor (optional: false): !bool,
    linkedin link: !url
}
"""

test_schema_with_quantity = """
!!temperature: !schema {
    t(description: The temperature of the room): !int (quantity: temperature)
}
"""

test_schema_with_description = """
!!person: !schema (
    name: "A Person", 
    description: "A description of a person",
    uuid : http://www.google.com
    ) {
    name(description: name of the person, optional: false): !str(min:3, max:25),
    age: !uint(min: 0, max: 125),
    minor (optional: false): !bool,
    linkedin link: !url
}
"""

test_schema_validation = """
{p: !!person {
        name: stephane,
        age: 25,
        minor: false
    }
}
"""

test_schema_validation_2 = """
{p: !!person {
        big age: !uint32 25,
        minor: !bool true,
        linkedin link : https://github.com/uon-language/uon-parser
    }
}
"""

test_schema_validation_yaml = """
p: !!person
  name: stephane
  age: 25
"""

uon_parser_2 = Lark.open(uon_2_grammar_file, parser='lalr',
                         postlex=TreeIndenter(), start='start', 
                         maybe_placeholders=True, debug=True)


def test():
    parse_tree = uon_parser_2.parse(test_schema_with_quantity)
    print(parse_tree.pretty(indent_str='  '))
    transformed = UON2RevisedTreeToPython().transform(parse_tree)
    print(transformed)
    with open("examples/Transform.txt", "w") as text_file:
        pprint(repr(transformed), stream=text_file)

    logging.debug(transformed.to_binary())
    logging.debug("\n")
    logging.debug(repr(transformed))
    logging.debug("\n")
    logging.debug(str(transformed))

    # TODO: remove
    # test_value = b"\x02\x12\x05\x00happy\x11\x03\x00yes\x12\x03\x00sad\x11\x02\x00no\x00"
    # logging.debug(decode_binary(test_value))
    # test_value_seq = b"\x01\x11\x05\x00happy\x11\x03\x00sad\x00"
    # logging.debug(decode_binary(test_value_seq))
    # test_simple_nested_map = (b'\x02\x12\x05\x00happy\x11\x03\x00yes\x12\x05\x00scale'
    #                         b'\x02\x12\x03\x00max$\x00\x00\x00\x00\x00\x00$@\x12\x03\x00min$'
    #                         b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    # logging.debug(decode_binary(test_simple_nested_map))
    # test_simple_nested_seq = b'\x01\x11\x01\x00a\x01\x11\x01\x00b\x11\x01\x00c\x00\x00'
    # logging.debug(decode_binary(test_simple_nested_seq))

    # logging.debug("\n")
    # logging.debug("\n")

    # v = Validator(UintTypeValidation(),
    #               [MinNumberValidation(0.0), MaxNumberValidation(125.0)],
    #               {})

    # logging.debug(v.to_binary())
    # logging.debug("\n")
    # logging.debug((b"\x1f\x19\x30\x0f\x15\x07" + struct.pack("<d", 0)
    #                + b"\x0f\x15\x08" + struct.pack("<d", 125)))

    # test_value = b"\x24\x00\x00\x00\x00\x00\x00i@\x00"
    # logging.debug(decode_binary_value(test_value))

if __name__ == '__main__':
    test()
