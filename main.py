from lark import Lark
from lark.reconstruct import Reconstructor
#from lark.tree import *

# Python module to pretty print Python data structures
from pprint import pprint

from parser.uon_parser import uon_parser, uon_parser_reconstructor

from transformer.tree_to_uon import TreeToUON 

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
    parse_tree = uon_parser.parse(data2)
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
    print("Transformed items")
    for k, v in transformed.items():
        print(k, v)
    print("Getting transformed[{}]: {}".format('bar', transformed['bar']))


    # Reconstruct the original text from the parse tree
    parse_tree_for_reconstruction = uon_parser_reconstructor.parse(data2)
    uon_emit = Reconstructor(uon_parser_reconstructor).reconstruct(parse_tree_for_reconstruction)
    with open("output/Emit.txt", "w") as text_file:
        text_file.write(uon_emit)

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

