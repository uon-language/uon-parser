from pathlib import Path

# Python module to pretty print Python data structures
from pprint import pprint

from lark import Lark
from lark.reconstruct import Reconstructor
#from lark.tree import *

from transformer.tree_to_uon import TreeToUON 

grammar_file = Path('grammar/uon_grammar.lark')

# The parser returned by Lark for our grammar.
# We have the maybe_placeholders option available in the Lark parser constructor, to handle optional fields
# in the rule so that they resolve to None if none is provided.
uon_parser = Lark.open(
    grammar_file,
    start='value',
    parser='lalr',
    maybe_placeholders=True,
)

# A parser instance with no maybe_placeholders because it causes an assertion error when reconstructing with it
uon_parser_reconstructor = Lark.open(
    grammar_file,
    start='value',
)

def main():
    text = '{"key": ["item0", "item1", 3.14, true]}'    
    data = """
    {
        foo(description="A Foo description"): !uint 42,
        bar: !num(unit: meters) 1123123412153121.41832154245214
    }
    """

    data2 = """
    {
        foo: !uint 42,
        bar(optional=true, description ="balala"): 30.7,
        tuf (description = "tuf tuf"): !uint !int !uint 10.5
    }
    """
    
    # Nested maps example
    data3 = """
        foo: 42,
        bar(optional=true, description ="balala"): {
            nestedmap : !uint !int !uint 56
        },
        tuf (description = "tuf tuf"): !int 10.5
    """

    # Sequences example
    data4 = """
        foo: - "hello"
        - "bye"
        - "sick"
    """

    # Description rule
    example2 = """(description= "baloney")"""

    # Parse the example with the grammar and return a parse tree (AST)
    parse_tree = uon_parser.parse(data3)
    print(parse_tree, end="\n")
    print()

    # Process the parse tree
    transformed = TreeToUON().transform(parse_tree)
    print()
    print("Transformed: ", transformed)
    print("Transformed type: ", type(transformed), end='\n')
    with open("output/Transform.txt", "w") as text_file:
        pprint(transformed, stream=text_file)

    # Some operations on the result dictionary
    """print("Transformed items")
    for k, v in transformed.items():
        print(k, v)
    print("Getting transformed[{}]: {}".format('bar', transformed['bar']))"""


    # Reconstruct the original text from the parse tree
    """parse_tree_for_reconstruction = uon_parser_reconstructor.parse(data2)
    uon_emit = Reconstructor(uon_parser_reconstructor).reconstruct(parse_tree_for_reconstruction)
    with open("output/Emit.txt", "w") as text_file:
        text_file.write(uon_emit)"""

    # Print the parse tree to file
    with open("output/Output.txt", "w") as text_file:
        text_file.write(parse_tree.pretty())

    #pydot__tree_to_png(parse_tree, "first_tree.png", "TB")

    #with open("Transform.txt", "w") as text_file:
        #text_file.write(str(transformed))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('kill')
        exit(0)

