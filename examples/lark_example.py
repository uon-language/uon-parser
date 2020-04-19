#
# This example shows how to write a basic UON parser for a simple UON example
#

from lark import Lark, Transformer
from lark.reconstruct import Reconstructor
#from lark.tree import *

# Python module to pretty print Python data structures
from pprint import pprint

# import custom made classes
from classes.uon_key import UonKey, UonKeyProperties

class UonPair(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
    def __str__(self):
        return str({
            self.key: self.value,
        })

uon_grammar = r"""
    ?value: dict
          | list
          | string
          | word
          | SIGNED_NUMBER      -> number
          | true
          | false
          | "null"             -> null

    list : "[" [value ("," value)*] "]"
    dict : "{" [pair ("," pair)*] "}" | [pair ("," pair)*]
    pair : pair_key ":" pair_value
    
    pair_key : (word | string) [key_properties]
    pair_value : [uon_type][unit] value

    key_properties: "(" [key_property ("," key_property)*] ")"
    key_property: required | description

    unit: "(unit:" word ")"
    description: "description" "="  string 
    required: "required" "=" (true | false) 
    uon_type: "!" word

    string : ESCAPED_STRING
    word : WORD
    true: "true"
    false: "false"

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %import common.WORD
    %ignore WS

    """

class TreeToUON(Transformer):
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
        if key[1] is None:
            # No key properties
            print("pair_key key: ", key[0], key[1], end='\n')
            return UonKey(key[0], {})
        return UonKey(key[0], key[1])
    def pair_value(self, value):
        print("visiting pair_value: ", value, ", pair_value items length: ", len(value), end="\n")
        return value

    def key_properties(self, properties):
        # Check if there is no properties, or by checking if the list has only None
        if not properties or all(e is None for e in properties):
            print("visiting key_properties: ", "No key_properties", end="\n")
            return {}
        else:
            # We will be receiving properties as a list of pairs
            print("visiting key_properties: ", properties, end="\n")
            return dict(properties)
    def key_property(self, property):
        print("visiting key_property", property, end='\n')
        return property[0]
    def description(self, value):
        print("visiting description: ", value, end="\n")
        return "description", value[0]
    def required(self, value):
        print("visiting required: ", value, end='\n')
        return "required", value[0]
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
        return dict(items)

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False

# The parser returned by Lark for our grammar.
# We have the maybe_placeholders option available in the Lark parser constructor, to handle optional fields
# in the rule so that they resolve to None if none is provided.
uon_parser = Lark(uon_grammar, start='value', lexer='standard', maybe_placeholders=True)

# A parser instance with no maybe_placeholders because it causes an error when reconstructing with it
uon_parser_reconstructor = Lark(uon_grammar, start='value', parser='lalr')

text = '{"key": ["item0", "item1", 3.14, true]}'    
data = """
{
    foo(description="A Foo description"): !uint 42,
    bar: !num(unit: meters) 1123123412153121.41832154245214
}
"""

data2 = """
{
    foo: 42,
    bar(required=true, description ="balala"): 30.7,
    tuf (description = "tuf tuf"): 10.5
}
"""

data3 = """
    foo: 42,
    bar(required=true, description ="balala"): {
        nestedmap : 56
    },
    tuf (description = "tuf tuf"): 10.5
"""

# Description rule
example2 = """(description= "baloney")"""

# Parse the example with the grammar and return a parse tree (AST)
parse_tree = uon_parser.parse(data3)
print(parse_tree, end="\n")

# Process the parse tree
transformed = TreeToUON().transform(parse_tree)
print("Transformed: ", transformed, end="\n")
print("Transformed type: ", type(transformed), end="\n")
with open("Transform.txt", "w") as text_file:
    pprint(transformed, stream=text_file)
#print("Transformed[0]", transformed['foo'], end='\n')

# Reconstruct the original text from the parse tree
parse_tree_for_reconstruction = uon_parser_reconstructor.parse(data3)
uon_emit = Reconstructor(uon_parser_reconstructor).reconstruct(parse_tree_for_reconstruction)
with open("Emit.txt", "w") as text_file:
    text_file.write(uon_emit)

# Print the parse tree to file
with open("Output.txt", "w") as text_file:
    text_file.write(parse_tree.pretty())

#pydot__tree_to_png(parse_tree, "first_tree.png", "TB")

#with open("Transform.txt", "w") as text_file:
    #text_file.write(str(transformed))

