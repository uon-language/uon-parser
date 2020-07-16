from pathlib import Path
from lark import Lark
from pprint import pprint

from transformer.uon_2_revised_tree_transformer import (
    UON2RevisedTreeToPython,
    TreeIndenter
)
from uonrevisedtypes.uon_custom_type import UonCustomType
from uonrevisedtypes.scalars.uon_uint import Uint64

from binary.codec import decode_binary

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

test_true_false = """
old: !bool false
young(optional : false): true
old: true
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
    h:1
"""

test_schema = """
!!person: schema {
    name(description: name of the person, optional: false): !str(min:3, max:25),
    age: !uint(min: 0, max: 125),
    minor (optional: false): !bool
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

test_schema_validation_yaml = """
p: !!person
  name: stephane
  age: 25
"""

uon_parser_2 = Lark.open(uon_2_grammar_file, parser='lalr',
                         postlex=TreeIndenter(), start='start', debug=True)


def test():
    parse_tree = uon_parser_2.parse(simple_mapping_example)
    print(parse_tree.pretty(indent_str='  '))
    transformed = UON2RevisedTreeToPython().transform(parse_tree)
    print(transformed)
    with open("examples/Transform.txt", "w") as text_file:
        pprint(transformed, stream=text_file)

    logging.debug(transformed.to_binary())

    test_value = b"\x02\x12\x05\x00happy\x11\x03\x00yes\x12\x03\x00sad\x11\x02\x00no\x00"
    logging.debug(decode_binary(test_value))
    test_value_seq = b"\x01\x11\x05\x00happy\x11\x03\x00sad\x00"
    logging.debug(decode_binary(test_value_seq))
    test_simple_nested_map = (b'\x02\x12\x05\x00happy\x11\x03\x00yes\x12\x05\x00scale'
                              b'\x02\x12\x03\x00max$\x00\x00\x00\x00\x00\x00$@\x12\x03\x00min$'
                              b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    logging.debug(decode_binary(test_simple_nested_map))
    test_simple_nested_seq = b'\x01\x11\x01\x00a\x01\x11\x01\x00b\x11\x01\x00c\x00\x00'
    logging.debug(decode_binary(test_simple_nested_seq))

if __name__ == '__main__':
    test()
