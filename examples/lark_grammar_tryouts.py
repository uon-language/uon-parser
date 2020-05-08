#
# This example demonstrates usage of the Indenter class.
#
# Since indentation is context-sensitive, a postlex stage is introduced to
# manufacture INDENT/DEDENT tokens.
#
# It is crucial for the indenter that the NL_type matches
# the spaces (and tabs) after the newline.
#

from pathlib import Path

from lark import Lark, Transformer, v_args
from lark.indenter import Indenter

python_grammar_file = Path('examples/python.lark')

tree_grammar_mapping = r"""
    ?start: _NL* _value
    _value : mapping* | NAME 
    mapping: NAME ":" _mapping_helper _NL*
    _mapping_helper: NAME | _NL _INDENT mapping+ _DEDENT 
    %import common.CNAME -> NAME
    %import common.WS_INLINE
    %declare _INDENT _DEDENT
    %ignore WS_INLINE
    _NL: /(\r?\n[\t ]*)+/
"""

tree_grammar_seq = r"""
    ?start: _NL* _value
    _value : seq* | name 
    seq : seq_item+
    seq_item: "-" _seq_helper _NL*
    _seq_helper : name | _NL _INDENT seq_item+ _DEDENT 
    name : NAME
    %import common.CNAME -> NAME
    %import common.WS_INLINE
    %declare _INDENT _DEDENT
    %ignore WS_INLINE
    _NL: /(\r?\n[\t ]*)+/
"""

tree_grammar_2 = r"""
    ?start: _NL* mapping
    mapping: NAME ":" _value
    _value: _NL [_INDENT mapping+ _DEDENT] | NAME
    %import common.CNAME -> NAME
    %import common.WS_INLINE
    %declare _INDENT _DEDENT
    %ignore WS_INLINE
    _NL: /(\r?\n[\t ]*)+/
"""

tree_grammar = r"""
    ?start: _NL* tree
    tree: NAME _NL [_INDENT tree+ _DEDENT]
    %import common.CNAME -> NAME
    %import common.WS_INLINE
    %declare _INDENT _DEDENT
    %ignore WS_INLINE
    _NL: /(\r?\n[\t ]*)+/
"""

class TreeIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8

class PythonIndenter(Indenter):
    NL_type = '_NEWLINE'
    OPEN_PAREN_types = ['LPAR', 'LSQB', 'LBRACE']
    CLOSE_PAREN_types = ['RPAR', 'RSQB', 'RBRACE']
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8

python_parser = Lark.open(
    python_grammar_file,
    parser='lalr', 
    postlex=PythonIndenter(),
    start='file_input'
)

parser = Lark(tree_grammar_seq, parser='lalr', postlex=TreeIndenter(), debug=True)

class TreeToSomething(Transformer):

    @v_args(inline=True)
    def name(self, string):
        print("visiting name: ", string)
        (s,) = string
        return s

    def seq(self, items):
        print("visiting seq: ", items)
        return items

    def seq_item(self, items):
        print("visiting seq items: ", items)
        return items

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False

test_python = """
if 2 == 2:
    True
else :
    False
"""

test_tree_mapping = """
a : 
    b : c
    d : e
f : g
"""

test_tree_seq = """
- 
  - a
  - b
- d
"""

test_tree_2 = """
a:
    b: bae
    c:
        d:boy
        e:girl
    f:
        g:wat
"""

test_tree = """
a
    b
    c
        d
        e
    f
        g
"""

def test():
    parse_tree = parser.parse(test_tree_seq)
    print(parse_tree.pretty())
    print(TreeToSomething().transform(parse_tree))

#def test():
#    print(python_parser.parse(test_python).pretty())

if __name__ == '__main__':
    test()