from pathlib import Path

from lark import Lark

from transformer.uon_2_revised_tree_transformer import (
    UON2RevisedTreeToPython,
    TreeIndenter
)

from serializer import python_to_uon

"""
TODO: Specify that this project is only compatible with Python 3.x
For example the str type is used heavily in this project and is used to
represent what was both plain strings and unicode in pre-Python3. But 
basestring is not available anymore in Python 3.x, str is now the type for 
everything that is string in Python. If we use Python 2.x, we might get
some unexpected behavior if we encounter unicode strings.

Another example is the difference in the purposes of some built-in methods.
For example the built-in method __nonzero__ in Python2 that determines the
truth value of an object, is now simply __bool__ in Python3.
"""
class UonParser:
    def __init__(self):
        uon_2_grammar_file = Path('grammar/uon_2_revised_grammar.lark')
        self.parser = Lark.open(uon_2_grammar_file, parser='lalr',
                                postlex=TreeIndenter(), 
                                maybe_placeholders=True, start='start')

    def load(self, filename, schema=None):
        transformer = UON2RevisedTreeToPython()
        # TODO: check filename ends in uon
        with open(filename) as f:
            read_data = f.read()
            parse_tree = self.parser.parse(read_data)

            if schema is not None:
                read_schema = f.read()
                schema_parse_tree = self.parser.parse(read_schema)
                transformer.transform(schema_parse_tree)

            transformed_tree = transformer.transform(parse_tree)

            return transformed_tree
            
    def parse(self, input_, schema_raw=None):
        transformer = UON2RevisedTreeToPython()
        parse_tree = self.parser.parse(input_)
        print(parse_tree.pretty(indent_str='  '))

        if schema_raw is not None:
            schema_parse_tree = self.parser.parse(schema_raw)
            print(schema_parse_tree.pretty(indent_str='  '))
            transformer.transform(schema_parse_tree)

        transformed_tree = transformer.transform(parse_tree)

        return transformed_tree

    def to_uon(self, input_):
        return python_to_uon(input_)


test_schema = """
!!person: !schema {
    name (description: name of the person, optional: false): !str(min:3,
     max:25),
    age: !uint(min: 0, max: 125),
    minor (optional: false): !bool,
    linkedin link: !url 
}
"""

test_schema_validation = """
{p: !!person {
        name: Stephane, 
        age: !uint32 25,
        minor: !bool true,
        linkedin link: www.google.com
    }
}
"""

test_schema_with_quantity = """
!!temperature: !schema {
    t(description: The temperature of the room): !int (quantity: temperature)
}
"""

test_schema_with_quantity_validation = """
{t: !!temperature {
    t: !int 32 km
    }
}

"""

# TODO: dynamically create classes for exceptions(maybe during compilation project)

def test():
    uon = UonParser()

    uon.parse(test_schema_with_quantity_validation, 
              schema_raw=test_schema_with_quantity)


if __name__ == '__main__':
    test()

