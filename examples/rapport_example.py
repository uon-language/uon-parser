import sys
from lark import Lark, Transformer

from pathlib import Path

# Python module to pretty print Python data structures
from pprint import pprint

class UonKey:
    def __init__(self, keyname, properties):
        self.keyname = keyname
        # or operator to return default value in case property is none
        # or any falsy value
        print("UonKey Constructor: ", keyname, properties)
        self.properties = properties
    
    def __repr__(self):
        return "{}: {{properties: {}}}".format(
            self.keyname, self.properties)

json_grammar = r"""
    ?value: dict
          | list
          | string
          | SIGNED_NUMBER      -> number
          | true
          | false
          | "null"             -> null

    list : "[" [value ("," value)*] "]"
    dict : "{" [pair ("," pair)*] "}"
    pair : pair_key ":" value
    
    pair_key : string [properties]

    properties: "(" [property ("," property)*] ")"
    property: optional | description

    description: "description" ":"  string 
    optional: "optional" ":" (true | false) 
    
    // Terminals
    string : ESCAPED_STRING
    true: "true"
    false: "false"

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS
    """

class TreeToJson(Transformer):
    def string(self, s):
        (s,) = s
        return s[1:-1]

    def number(self, n):
        (n,) = n
        return float(n)

    def pair(self, key_value):
        k, v = key_value
        return k, v

    def pair_key(self, key):
        if key[1] is None:
            # No key properties
            return UonKey(key[0], {})
        return UonKey(key[0], key[1])

    def properties(self, properties):
        # Check if there is no properties, or by checking if the list has only None
        if not properties or all(e is None for e in properties):
            return {}
        else:
            # We will be receiving properties as a list of pairs
            return dict(properties)

    def property(self, property):
        """
        Return the property
        """
        return property[0]

    def description(self, value):
        """
        Return a description property as a tuple of keyword "description" 
        and its value
        """
        return "description", value[0]

    def optional(self, value):
        """
        Return an optional property as a tuple of keyword "optional" 
        and its value
        """
        return "optional", value[0]
        
    # pair = tuple
    # dict = dict
    list = list

    def dict(self, items):
        return dict(items)

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False

json_parser = Lark(json_grammar, start='value', lexer='standard')

test_data = '{"key" (optional: true, description: "A key", optional: false): ["item0", "item1", 3.14]}'

tree = json_parser.parse(test_data)
print(tree.pretty())

# Print the parse tree to file
with open("examples/rapport.txt", "w") as text_file:
    text_file.write(tree.pretty())

print(TreeToJson().transform(tree))