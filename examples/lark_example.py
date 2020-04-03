#
# This example shows how to write a basic UON parser for a simple UON example
#

from lark import Lark
from lark.reconstruct import Reconstructor
#from lark.tree import *

uon_parser = Lark(r"""
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
    pair : word [description] ":" [type][unit] value

    unit: "(unit:" word ")"
    description: "(description="  string ")"
    type: "!" cname

    string : ESCAPED_STRING
    word : WORD
    cname: CNAME

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %import common.WORD
    %import common.CNAME
    %ignore WS

    """, start='value')

text = '{"key": ["item0", "item1", 3.14, true]}'    

data = """
{
    foo(description="A Foo description"): !uint32 42,
    bar: !num(unit: meters) 1123123412153121.41832154245214
}
"""

parse_tree = uon_parser.parse(data)

print(parse_tree)

uon_emit = Reconstructor(uon_parser).reconstruct(parse_tree)
with open("Emit.txt", "w") as text_file:
    text_file.write(uon_emit)

#pydot__tree_to_png(parse_tree, "first_tree.png", "TB")

with open("Output.txt", "w") as text_file:
    text_file.write(parse_tree.pretty())

