from pathlib import Path

from lark import Lark

from pprint import pprint

from transformer.uon_2_revised_tree_transformer import (
    UON2RevisedTreeToPython,
    TreeIndenter
)

uon_2_grammar_file = Path('grammar/uon_2_revised_grammar.lark')

test_json = """
{foo : 42,
bar: {
    hey: ho,
    boy: hood
},
l : [one, 2, three]}
"""

test_uon = """
foo: 42
json:
    h:1
"""

schema = """
!!person: schema {
    name: !str(min:3, max:25),
    age: !uint(min: 100.5, max: 125)
}
"""

test_schema = """
p: !!mapping
  a : s
  d : e
"""

uon_parser_2 = Lark.open(uon_2_grammar_file, parser='lalr',
                         postlex=TreeIndenter(), start='start', debug=True)


def test():
    parse_tree = uon_parser_2.parse(test_schema)
    print(parse_tree.pretty(indent_str='  '))
    transformed = UON2RevisedTreeToPython().transform(parse_tree)
    print(transformed)
    with open("examples/Transform.txt", "w") as text_file:
        pprint(transformed, stream=text_file)


if __name__ == '__main__':
    test()
