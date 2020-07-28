import sys
from lark import Lark, Transformer

simple_grammar = r"""
?value: hello w_word | hello world
w_word: /\bw(.)*/
world: "world"
hello: "hello"

%import common.WS
%ignore WS
"""

test_parser = Lark(simple_grammar, start='value', parser='lalr', lexer="standard")
tree_simple = test_parser.parse('hello world')
print(tree_simple.pretty(indent_str=" "))
