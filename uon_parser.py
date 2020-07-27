from pathlib import Path
from lark import Lark

from transformer.uon_2_revised_tree_transformer import (
    UON2RevisedTreeToPython,
    UonIndenter
)

from serializer import python_to_uon

from binary.codec import decode_binary, decode_schema

import logging
logging.basicConfig(level=logging.DEBUG)

UON_GRAMMAR_FILE = Path('grammar/uon_2_revised_grammar.lark')


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

Another feature of Python3 is that dicts are now ordered as of Python 3.6.
"""


def load(input_, schemas={}, show_tree=False, debug=False):
    return UonParser(schemas=schemas).load(
        input_, show_tree=show_tree, debug=debug
    )


def load_from_file(self, filename, show_tree=False, debug=False):
    return UonParser().load_from_file(filename, show_tree=show_tree,
                                      debug=debug)


def dump(input_):
    return UonParser().dump(input_)


def dump_to_file(self, input_, filename):
    UonParser().dump_to_file(input_, filename)


def validate(input_, schema_raw=None, show_tree=False, debug=False):
    parser = UonParser()

    if schema_raw is not None:
        # Schema will be saved in the parser
        parser.load(schema_raw, show_tree=show_tree, debug=debug)

    return parser.load(input_, show_tree=show_tree, debug=debug)


def to_binary(self, uon_input):
    return UonParser().to_binary(uon_input)


def from_binary(self, binary_input, schemas={}):
    return UonParser(schemas).from_binary(binary_input)


class UonParser:
    """ A parser for Uon. The parser saves all the schemas that it parses,
    for validation on further inputs.

    You should use this class if you want to hold on to the schemas that you
    provide it using load_schema() or schema_from_binary().
    These schemas will be used to validate further uon inputs
    automatically.
    """
    def __init__(self, schemas={}):
        self.parser = Lark.open(UON_GRAMMAR_FILE, parser='lalr',
                                postlex=UonIndenter(),
                                maybe_placeholders=True, start='start')
        self.transformer = UON2RevisedTreeToPython()
        self.schemas = schemas

    def load(self, input_, show_tree=False, debug=False):
        parse_tree = self.parser.parse(input_)
        if show_tree:
            logging.debug(parse_tree.pretty(indent_str=" "))
        self.transformer.debug = debug
        transformed = self.transformer.transform(parse_tree)

        # Revert transformer debug back to default
        self.transformer.debug = False
        return transformed

    def load_from_file(self, filename, show_tree=False, debug=False):
        if not filename.endswith(".uon"):
            raise ValueError("Not a .uon file")
        with open(filename) as f:
            read_data = f.read()
            return self.load(read_data, show_tree=show_tree, debug=debug)

    def load_schema(self, schema_raw, show_tree=False, debug=False):
        schema = self.load(schema_raw, show_tree=show_tree, debug=debug)
        self.schemas[schema.type_] = schema
        return schema

    def load_schema_from_file(self, filename, show_tree=False, debug=False):
        if not filename.endswith(".uon"):
            raise ValueError("Not a .uon file")
        with open(filename) as f:
            read_data = f.read()
            return self.load_schema(read_data, show_tree=show_tree,
                                    debug=debug)

    def dump(self, input_):
        return python_to_uon(input_)

    def dump_to_file(self, input_, filename):
        if not filename.endswith(filename):
            filename += ".uon"
        with open(filename, "w") as file_stream:
            file_stream.write(self.dump(input_))

    def to_binary(self, uon_input):
        parsed_uon = self.load(uon_input)
        return parsed_uon.to_binary()

    def from_binary(self, binary_input):
        return decode_binary(binary_input, schemas=self.schemas)

    def schema_from_binary(self, binary_schema):
        schema = decode_schema(binary_schema)
        self.schemas[schema.type_] = schema
        return schema
