from pathlib import Path

from lark import Lark

grammar_file = Path.cwd() / 'parser' / 'uon_grammar.lark'

# The parser returned by Lark for our grammar.
# We have the maybe_placeholders option available in the Lark parser constructor, to handle optional fields
# in the rule so that they resolve to None if none is provided.
uon_parser = Lark.open(
    grammar_file,
    start='value',
    lexer='standard',
    maybe_placeholders=True,
)

# A parser instance with no maybe_placeholders because it causes an assertion error when reconstructing with it
uon_parser_reconstructor = Lark.open(
    grammar_file,
    start='value',
    lexer='standard'
)