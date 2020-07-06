from pathlib import Path

from lark import Lark

from transformer.uon_2_revised_tree_transformer import (
    UON2RevisedTreeToPython,
    TreeIndenter
)

"""
TODO: Specify that this project is only compatible with Python 3.x
For example the str type is used heavily in this project and is used to
represent what was both plain strings and unicode in pre-Python3. But 
basestring is not available anymore in Python 3.x, str is now the type for 
everything that is string in Python. If we use Python 2.x, we might get
some unexpected behavior if we encounter unicode strings.
"""
class Uon:
    def __init__(self):
        uon_2_grammar_file = Path('grammar/uon_2_revised_grammar.lark')
        self.parser = Lark.open(uon_2_grammar_file, parser='lalr',
                                postlex=TreeIndenter(), start='start')

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

        if schema_raw is not None:
            schema_parse_tree = self.parser.parse(schema_raw)
            transformer.transform(schema_parse_tree)

        transformed_tree = transformer.transform(parse_tree)

        return transformed_tree


test_schema = """
!!person: schema {
    name: !str(min:3, max:25),
    age: !uint(min: 0, max: 125)
}
"""

test_schema_validation = """
{p: !!person {
        name: stephane,
        age: !uint32 130
    }
}
"""

# TODO: dynamically create classes for exceptions(maybe during compilation project)

def test():
    uon = Uon()

    uon.parse(test_schema_validation, schema_raw=test_schema)


if __name__ == '__main__':
    test()

