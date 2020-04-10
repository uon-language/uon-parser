import sys
from lark import Lark, Transformer

json_grammar = r"""
    ?value: dict
          | list
          | string
          | SIGNED_NUMBER      -> number
          | "true"             -> true
          | "false"            -> false
          | "null"             -> null

    list : "[" [value ("," value)*] "]"

    dict : "{" [pair ("," pair)*] "}"
    pair : string ":" value

    string : ESCAPED_STRING

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

    def list(self, items):
        print("visiting list: ", items, end="\n")
        return list(items)
    def pair(self, key_value):
        print("visiting pair: ", key_value, end="\n")
        k, v = key_value
        return k, v
    def dict(self, items):
        print("visiting dict: ", items, end="\n")
        return dict(items)

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False

json_parser = Lark(json_grammar, start='value', lexer='standard')

test_data = '{"key": ["item0", "item1", 3.14]}'

tree = json_parser.parse(test_data)
print(TreeToJson().transform(tree))