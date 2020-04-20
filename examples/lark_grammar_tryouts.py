import sys
from lark import Lark, Transformer

# A simple grammar to test indentation and optional braces

json_grammar = r"""
    ?value: dict
          | string
          | SIGNED_NUMBER      -> number
          | "true"             -> true
          | "false"            -> false
          | "null"             -> null

    dict : "{" [pair ("," pair)*] "}" | [pair ("," pair)*]
    pair : string ":" value

    string : ESCAPED_STRING

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS
    """

json_parser = Lark(json_grammar, start='value', lexer='standard')

test_data = '"key": "item0"'

tree = json_parser.parse(test_data)