#
# This example shows how to write a basic UON parser for a simple UON example
#

from lark import Lark, Transformer
from lark.reconstruct import Reconstructor
#from lark.tree import *

class UonPair(object):
    def __init__(self, key, value, description, uonType, unit):
        self.key = key
        self.value = value
        self.description = description
        self.uonType = uonType
        self.unit = unit

    def __str__(self):
        return str({
            self.key: self.value,
            "description": self.description,
            "unit": self.unit,
            "type": self.uonType
        })

uon_grammar = r"""
    ?value: dict
          | list
          | string
          | word
          | SIGNED_NUMBER      -> number
          | "true"             -> true
          | "false"            -> false
          | "null"             -> null

    list : "[" [value ("," value)*] "]"
    dict : "{" [pair ("," pair)*] "}"
    pair : (word | string) [description] ":" [type][unit] value

    unit: "(unit:" word ")"
    description: "(description="  string ")"
    type: "!" word

    UNIT_KEYWORD : "unit"
    DESCRIPTION_KEYWORD : "description"

    string : ESCAPED_STRING
    word : WORD

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %import common.WORD
    %ignore WS

    """

class TreeToUON(Transformer):
    '''def list(self, items):
        return list(items)
    def pair(self, key_value):
        print(key_value, end="\n")
        k, v = key_value
        print(key_value, end="\n")
        return k, v
    def dict(self, items):
        return dict(items)
    def description(self, items):
        print(items, end="\n")
        d = ["description", items]
        return d
    def unit(self, items):
        print(items, end="\n")
        d = ["unit", items]
        return d

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False'''
    def string(self, s):
        print(s, end="\n")
        (s,) = s
        print("decomposing: " + s, end="\n")
        return s[1:-1]
    def number(self, n):
        print(n, end="\n")
        (n,) = n
        return float(n)

    def description(self, value):
        print(value, end='\n')
        return value

    list = list
    pair = tuple
    dict = dict

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False

# The parser returned by Lark for our grammar
uon_parser = Lark(uon_grammar, start='value', lexer='standard')
text = '{"key": ["item0", "item1", 3.14, true]}'    
data = """
{
    foo(description="A Foo description"): !uint 42,
    bar: !num(unit: meters) 1123123412153121.41832154245214
}
"""
# Description rule
example2 = """(description= "baloney")"""

parse_tree = uon_parser.parse(data)
print(parse_tree, end="\n")

transformed = TreeToUON().transform(parse_tree)
print(transformed, end="\n")

# Reconstruct the original text from the parse tree
uon_emit = Reconstructor(uon_parser).reconstruct(parse_tree)
with open("Emit.txt", "w") as text_file:
    text_file.write(uon_emit)

#pydot__tree_to_png(parse_tree, "first_tree.png", "TB")

with open("Output.txt", "w") as text_file:
    text_file.write(parse_tree.pretty())

#with open("Transform.txt", "w") as text_file:
    #text_file.write(transformed.pretty())

