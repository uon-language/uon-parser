import json
import timeit

mysetup_json_big = '''import json
data = """{
    "name": "Jack",
    "age" : 28, 
    "hobbies" : ["skating", "eating", "jogging"],
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut  labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia  deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut  labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia  deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut  labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia  deserunt mollit anim id est laborum."
}"""
'''
s_json = ''' 
b = json.loads(data)
'''

print("JSON time: ", timeit.timeit(setup=mysetup_json_big, stmt= s_json, number=10000))

my_setup_lark_big = '''
from lark import Lark, Transformer

json_grammar = r"""
    ?value: dict
          | list
          | string
          | SIGNED_NUMBER      -> number
          | "true"             -> true
          | "false"            -> false
          | "null"             -> null

    list : "[" [value ("," value)*] "]"

    dict : "{" [pair ("," pair)*] "}"
    pair : string ":" value

    string : ESCAPED_STRING

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS
    """


class TreeToJson(Transformer):
    def string(self, s):
        (s,) = s
        return s[1:-1]

    def number(self, n):
        (n,) = n
        return float(n)

    def list(self, items):
        return list(items)

    def pair(self, key_value):
        k, v = key_value
        return k, v
        
    def dict(self, items):
        return dict(items)

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False

json_parser = Lark(json_grammar, start='value',
                   parser='lalr', lexer='standard')

test_data = """{
    "name": "Jack",
    "age" : 28, 
    "hobbies" : ["skating", "eating", "jogging"],
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut  labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia  deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut  labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia  deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut  labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia  deserunt mollit anim id est laborum."
}"""
'''

stmt_lark = '''
tree = json_parser.parse(test_data)
TreeToJson().transform(tree)
'''
print("Lark time: ", timeit.timeit(setup=my_setup_lark_big, stmt=stmt_lark, number=10000))

my_setup_lark = '''
from lark import Lark, Transformer

json_grammar = r"""
    ?value: dict
          | list
          | string
          | SIGNED_NUMBER      -> number
          | "true"             -> true
          | "false"            -> false
          | "null"             -> null

    list : "[" [value ("," value)*] "]"

    dict : "{" [pair ("," pair)*] "}"
    pair : string ":" value

    string : ESCAPED_STRING

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS
    """


class TreeToJson(Transformer):
    def string(self, s):
        (s,) = s
        return s[1:-1]

    def number(self, n):
        (n,) = n
        return float(n)

    def list(self, items):
        return list(items)

    def pair(self, key_value):
        k, v = key_value
        return k, v
        
    def dict(self, items):
        return dict(items)

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False

json_parser = Lark(json_grammar, start='value',
                   parser='lalr', lexer='standard')

test_data = '{"key": ["item0", "item1", 3.14]}'
'''

stmt_lark = '''
tree = json_parser.parse(test_data)
TreeToJson().transform(tree)
'''
print("Lark time: ", timeit.timeit(setup=my_setup_lark, stmt=stmt_lark, number=10000))

mysetup_json_small = '''import json
data = '{"key": ["item0", "item1", 3.14]}'
'''

s_json = ''' 
b = json.loads(data)
'''

print("JSON time: ", timeit.timeit(setup=mysetup_json_small, stmt=s_json, number=10000))

mysetup_json_medium = '''import json
data = """{
    "name": "Jack",
    "age" : 28, 
    "hobbies" : ["skating", "eating", "jogging"],
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut  labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia  deserunt mollit anim id est laborum."
    }"""
'''
s_json = ''' 
b = json.loads(data)
'''

print("JSON time: ", timeit.timeit(setup=mysetup_json_medium, stmt=s_json, number=10000))

my_setup_lark_medium = '''
from lark import Lark, Transformer

json_grammar = r"""
    ?value: dict
          | list
          | string
          | SIGNED_NUMBER      -> number
          | "true"             -> true
          | "false"            -> false
          | "null"             -> null

    list : "[" [value ("," value)*] "]"

    dict : "{" [pair ("," pair)*] "}"
    pair : string ":" value

    string : ESCAPED_STRING

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS
    """


class TreeToJson(Transformer):
    def string(self, s):
        (s,) = s
        return s[1:-1]

    def number(self, n):
        (n,) = n
        return float(n)

    def list(self, items):
        return list(items)

    def pair(self, key_value):
        k, v = key_value
        return k, v
        
    def dict(self, items):
        return dict(items)

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False

json_parser = Lark(json_grammar, start='value',
                   parser='lalr', lexer='standard')

test_data = """{
    "name": "Jack",
    "age" : 28, 
    "hobbies" : ["skating", "eating", "jogging"],
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut  labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia  deserunt mollit anim id est laborum."
    }"""
'''

stmt_lark = '''
tree = json_parser.parse(test_data)
TreeToJson().transform(tree)
'''
print("Lark time: ", timeit.timeit(setup=my_setup_lark_medium, stmt=stmt_lark, number=10000))

my_setup_lark_treeless = '''
from lark import Lark, Transformer

json_grammar = r"""
    ?value: dict
          | list
          | string
          | SIGNED_NUMBER      -> number
          | "true"             -> true
          | "false"            -> false
          | "null"             -> null

    list : "[" [value ("," value)*] "]"

    dict : "{" [pair ("," pair)*] "}"
    pair : string ":" value

    string : ESCAPED_STRING

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS
    """


class TreeToJson(Transformer):
    def string(self, s):
        (s,) = s
        return s[1:-1]

    def number(self, n):
        (n,) = n
        return float(n)

    def list(self, items):
        return list(items)

    def pair(self, key_value):
        k, v = key_value
        return k, v
        
    def dict(self, items):
        return dict(items)

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False

json_parser = Lark(json_grammar, start='value',
                   parser='lalr', lexer='standard',
                   transformer=TreeToJson())

test_data = """{
    "name": "Jack",
    "age" : 28, 
    "hobbies" : ["skating", "eating", "jogging"],
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut  labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia  deserunt mollit anim id est laborum."
    }"""
'''

stmt_lark = '''
tree = json_parser.parse(test_data)
'''
print("Lark time: ", timeit.timeit(setup=my_setup_lark_medium, stmt=stmt_lark, number=10000))