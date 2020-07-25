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


class UonParser:
    def __init__(self, schemas={}):
        self.parser = Lark.open(UON_GRAMMAR_FILE, parser='lalr',
                                postlex=UonIndenter(),
                                maybe_placeholders=True, start='start')
        self.transformer = UON2RevisedTreeToPython()

    def load(self, input_, show_tree=False, debug=False):
        parse_tree = self.parser.parse(input_)
        if show_tree:
            logging.debug(parse_tree.pretty(indent_str=" "))
        transformed = self.transformer.transform(parse_tree)
        return transformed

    def load_from_file(self, filename, show_tree=False, debug=False):
        if not filename.endswith(".uon"):
            raise ValueError("Not a .uon file")
        with open(filename) as f:
            read_data = f.read()
            return self.load(read_data, show_tree=show_tree, debug=debug)

    def load_schema(self, schema_raw):
        return self.load(schema_raw)

    def load_schema_from_file(self, filename):
        return self.load_from_file(filename)

    def parse(self, input_, schema_raw):
        return ""

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
