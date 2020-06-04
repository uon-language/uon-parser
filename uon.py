from pathlib import Path

from lark import Lark

from transformer.uon_2_tree_transformer import UON2TreeToPython, TreeIndenter


class Uon:
    def __init__(self):
        uon_2_grammar_file = Path('grammar/uon_2_grammar.lark')
        self.parser = Lark.open(uon_2_grammar_file, parser='lalr',
                                postlex=TreeIndenter(), start='start')
        self.transformer = UON2TreeToPython()
