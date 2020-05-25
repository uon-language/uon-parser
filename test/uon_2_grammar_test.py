from pathlib import Path

from lark import Lark, Transformer, v_args
from lark.indenter import Indenter

from pprint import pprint

uon_2_grammar_file = Path('grammar/uon_2_grammar.lark')


class TreeIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8


class UON2TreeToPython(Transformer):

    @v_args(inline=True)
    def name(self, string):
        print("visiting name: ", string)
        (s,) = string
        return s

    @v_args(inline=True)
    def string(self, string):
        print("visiting string: ", string)
        return string.strip()

    def seq_item(self, items):
        print("visiting seq items: ", items)
        return items[0]

    def top_map(self, mapping):
        print("visiting tree_mapping: ", mapping)
        return dict(mapping)

    def top_seq(self, seq):
        print("visiting top_seq: ", seq)
        return seq

    def pair(self, pair):
        print("visiting pair: ", pair)
        p = (pair[0], pair[1])
        return p

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False


test_uon_2 = """
a (description = A key) : d
b : e
c : f
"""

uon_parser_2 = Lark.open(uon_2_grammar_file, parser='lalr',
                         postlex=TreeIndenter(), start='start', debug=True)


def test():
    parse_tree = uon_parser_2.parse(test_uon_2)
    print(parse_tree.pretty(indent_str='  '))
    transformed = UON2TreeToPython().transform(parse_tree)
    print(transformed)
    with open("examples/Transform.txt", "w") as text_file:
        pprint(transformed, stream=text_file)


if __name__ == '__main__':
    test()
