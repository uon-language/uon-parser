from pathlib import Path
from lark import Lark
from pprint import pprint

from transformer.uon_tree_transformer import (
    UonTreeToPython,
    UonIndenter
)

from binary.codec import (
    decode_binary, decode_binary_value,
    decode_schema
)

import logging
logging.basicConfig(level=logging.DEBUG)

uon_grammar_file = Path('grammar/uon_grammar.lark')

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
    min:
        scale: 10
        value: 2
sad: no
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

test_punctuated_strings = r"""
{
    a : "a punctuated {}(),?[] string but we cannot put quotes",
    b : We can put not put commas inside unescaped strings but we can put ?!"',
    c : ''
}
"""

test_number_in_strings = """
a : number is 3
b : !str 3
c : -3
"""

test_simple_number = """
c : 32 K
"""

test_regex = """
a : /asdnaksdl/
"""

test_true_false = """
old: !bool false
young(description: "are we young?", description: "yes", optional : false): !str true
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
bad: "32"
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
    t(description: The temperature of the room,
         optional : false): !int (quantity: temperature)
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
        name: Stephane, 
        age: !uint32 25,
        minor: !bool true,
        linkedin link: www.google.com,
        s: hole
    }
}
"""

test_schema_validation_2 = """
{
    p: !!person {
        big age: !uint32 25,
        minor: !bool true,
        linkedin link : https://github.com/uon-language/uon-parser
    },
    q: !!person {
        big age: !uint32 24,
        minor: !bool false,
        linkedin: https://hello.com
    },
    something: Ok
}
"""

test_schema_validation_yaml = """
p: !!person
  name: stephane
  age: 25
"""

uon_parser_2 = Lark.open(uon_grammar_file, parser='lalr',
                         postlex=UonIndenter(), start='start', 
                         maybe_placeholders=True, debug=True)


def parse_test():
    parse_tree = uon_parser_2.parse(test_simple_number)
    print(parse_tree.pretty(indent_str='  '))
    transformed = UonTreeToPython(debug=True).transform(parse_tree)
    print(transformed)
    with open("examples/Transform.txt", "w") as text_file:
        pprint(repr(transformed), stream=text_file)

    transformed_to_binary = transformed.to_binary()
    logging.debug(transformed_to_binary)
    logging.debug("\n")
    logging.debug(repr(transformed))
    logging.debug("\n")
    logging.debug(str(transformed))


if __name__ == '__main__':
    parse_test()
