#
# This example shows how to write a basic UON parser for a simple UON example
#

from lark import Lark, Transformer
from lark.reconstruct import Reconstructor
#from lark.tree import *

# Python module to pretty print Python data structures
from pprint import pprint

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
            "uon_type": self.uonType
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
    pair : pair_key ":" pair_value
    
    pair_key : (word | string) [description]
    pair_value : [uon_type][unit] value

    unit: "(unit:" word ")"
    description: "(description="  string ")"
    uon_type: "!" word

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
        print("visiting string: ", s, end="\n")
        (s,) = s
        return s[1:-1]
    def number(self, n):
        print("visiting number: ", n, end="\n")
        (n,) = n
        return float(n)
    def word(self, s):
        print("visiting word: ", s, end="\n")
        (s,) = s
        return s[0:]

    def pair(self, key_value):
        k, v = key_value
        print("visiting pair: ", key_value, ", pair items length: ", len(key_value), end="\n")
        return k, v
    def pair_key(self, key):
        print("visiting pair_key: ", key, ", pair_key items length: ", len(key), end="\n")
        return key
    def pair_value(self, value):
        print("visiting pair_value: ", value, ", pair_value items length: ", len(value), end="\n")
        return value

    def description(self, value):
        print("visiting description: ", value, end="\n")
        return dict(description=value[0])
    def unit(self, value):
        print("visiting unit: ", value, end="\n")
        return dict(unit=value[0])
    def uon_type(self, value):
        print("visiting uon_type: ", value, end="\n")
        return dict(type=value[0])
        
    #pair = tuple
    #dict = dict
    list = list
    def dict(self, items):
        print("visiting dict: ", items, end="\n")
        return items

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

data2 = """
{
    foo(description="A foo description"): 42,
    bar: 30.7
}
"""
# Description rule
example2 = """(description= "baloney")"""

# Parse the example with the grammar and return a parse tree (AST)
parse_tree = uon_parser.parse(data)
print(parse_tree, end="\n")

# Process the parse tree
transformed = TreeToUON().transform(parse_tree)
print("Transformed: ", transformed, end="\n")
print("Transformed type: ", type(transformed), end="\n")
with open("Transform.txt", "w") as text_file:
    pprint(transformed, stream=text_file)
#print("Transformed[0]", transformed['foo'], end='\n')

# Reconstruct the original text from the parse tree
uon_emit = Reconstructor(uon_parser).reconstruct(parse_tree)
with open("Emit.txt", "w") as text_file:
    text_file.write(uon_emit)

# Print the parse tree to file
with open("Output.txt", "w") as text_file:
    text_file.write(parse_tree.pretty())

#pydot__tree_to_png(parse_tree, "first_tree.png", "TB")

#with open("Transform.txt", "w") as text_file:
    #text_file.write(str(transformed))

