from pathlib import Path

from lark import Lark

from transformer.uon_2_tree_transformer import UON2TreeToPython, TreeIndenter


class Uon:
    def __init__(self):
        uon_2_grammar_file = Path('grammar/uon_2_grammar.lark')
        self.parser = Lark.open(uon_2_grammar_file, parser='lalr',
                                postlex=TreeIndenter(), start='start')
        self.transformer = UON2TreeToPython()

    def load(self, filename):
        with open(filename) as f:
            read_data = f.read()
            parse_tree = self.parser.parse(read_data)
            transformed_tree = self.transformer.transform(parse_tree)
            return transformed_tree
            
    def parse(self, input):
        parse_tree = self.parser.parse(input)
        transformed_tree = self.transformer.transform(parse_tree)
        return transformed_tree
