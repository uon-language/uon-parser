from pathlib import Path

from lark import Lark
from lark.indenter import Indenter

python_grammar_file = Path('examples/python.lark')


class PythonIndenter(Indenter):
    NL_type = '_NEWLINE'
    OPEN_PAREN_types = ['LPAR', 'LSQB', 'LBRACE']
    CLOSE_PAREN_types = ['RPAR', 'RSQB', 'RBRACE']
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8


python_parser = Lark.open(
    python_grammar_file,
    parser='lalr', 
    postlex=PythonIndenter(),
    start='file_input'
)

test_python = """
if (2 == 
2):
        print(True)
else:
    print(False)
"""


def test():
    print(python_parser.parse(test_python).pretty(indent_str='  '))


if __name__ == '__main__':
    test()