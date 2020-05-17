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

from pprint import pprint

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

test_tree_map = """
a : d
b : e
c : f
"""

test_tree_nested_mapping = """
a : 
    b : c
    d : e
f : g
"""

tree_grammar_seq = r"""
    ?start: _NL* _value
    _value : seq_item* | name 
    seq_item: "-" name (_NL ("-" name | _seq_helper) (_NL)*)*
    _seq_helper : _INDENT seq_item+ _DEDENT 
    name : NAME
    %import common.CNAME -> NAME
    %import common.WS_INLINE
    %declare _INDENT _DEDENT
    %ignore WS_INLINE
    _NL: /(\r?\n[\t ]*)+/
"""

test_tree_seq = """
- a
- b
- c
"""

test_tree_nested_seq = """
-
    - d
    - s
- 
    - e
    - s
- r
- s
"""

tree_grammar_all = r"""
    ?start: _NL* _value+ 
    _value : tree_mapping | tree_seq
    tree_mapping: NAME ":" ((NAME _NL+) | (_NL [_INDENT _value+ _DEDENT]))
    tree_seq : "-" ((NAME _NL+) | (_NL [_INDENT _value+ _DEDENT]))
    %import common.CNAME -> NAME
    %import common.WS_INLINE
    %declare _INDENT _DEDENT
    %ignore WS_INLINE
    _NL: /(\r?\n[\t ]*)+/
"""

test_grammar_with_empty_nodes = """
a :
    b : c
    d : 
        q : 
    d :
f : g
"""

test_grammar_with_empty_nodes_2 = """
a : d
b : 
c : e
"""

test_grammar_valid = """
a :
    - b
    - c
b : 
    - d
    - e
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

parser = Lark(tree_grammar_all, parser='lalr', postlex=TreeIndenter(), debug=True)

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

    def tree_mapping(self, mapping):
        print("visiting tree_mapping: ", mapping)
        return mapping

    def tree_seq(self, seq):
        print("visiting tree_seq: ", seq)
        flat_list = [item for sublist in seq for item in sublist]
        return flat_list

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False

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
    parse_tree = parser.parse(test_grammar_with_empty_nodes_2)
    print(parse_tree.pretty(indent_str='  '))
    transformed = TreeToSomething().transform(parse_tree)
    print(transformed)
    with open("examples/Transform.txt", "w") as text_file:
        pprint(transformed, stream=text_file)

if __name__ == '__main__':
    test()