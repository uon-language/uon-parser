from lark import Transformer, v_args
from lark.indenter import Indenter

from uonrevisedtypes.uon_pair_key import UonPairKey, UonPairKeyProperties
from uonrevisedtypes.uon_pair import UonPair
from uonrevisedtypes.scalars.uon_float import Float64
from uonrevisedtypes.type_coercion import type_constructors
from uonrevisedtypes.collections.uon_dict import UONDictionary


class TreeIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = ['LPAR', 'LSQB', 'LBRACE']
    CLOSE_PAREN_types = ['RPAR', 'RSQB', 'RBRACE']
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8


class UON2RevisedTreeToPython(Transformer):

    @v_args(inline=True)
    def name(self, string):
        print("visiting name: ", string)
        (s,) = string
        return s
        
    def escaped_string(self, s):
        print("visiting escaped string: ", s)
        # (s,) = s
        # return s[1:-1].replace('\\"', '"')
        s = ' '.join(s)
        print("joining string: ", s)
        return s

    def string(self, string):
        print("visiting string: ", string)
        s = ' '.join(string)
        print("joining string: ", s)
        return s

    @v_args(inline=True)
    def number(self, n):
        print("visiting number: ", n)
        return Float64(n)

    def yaml_mapping(self, mapping):
        print("visiting yaml mapping: ", mapping)
        return UONDictionary(mapping)

    def json_mapping(self, mapping):
        print("visiting json mapping: ", mapping)
        return UONDictionary(mapping)

    def yaml_seq(self, seq):
        print("visiting yaml seq: ", seq)
        return seq
    
    def json_seq(self, seq):
        print("visiting json seq: ", seq)
        return seq

    def seq_item(self, items):
        print("visiting seq items: ", items)
        return items[0]

    def pair(self, pair):
        print("visiting pair: ", pair)
        return pair[0].keyname, UonPair(pair[0], pair[1])

    def json_pair(self, pair):
        print("visiting json pair: ", pair)
        return pair[0].keyname, UonPair(pair[0], pair[1])

    def pair_key(self, key):
        print("visiting pair_key: ", key)
        return UonPairKey(key[0], key[1] if 1 < len(key) else None)
    
    def presentation_properties(self, properties):
        """
        We will be receiving properties as a list of pairs.
        We transform the properties into a dictionary of properties names
        and their values. That way, if a certain property is repeated,
        it will keep only its last value.
        """
        print("visiting key_properties: ", properties, end="\n")
        properties = dict(properties)
        description = properties.get("description")
        optional = properties.get("optional", False)
        return UonPairKeyProperties(description, optional)

    @v_args(inline=True)
    def description(self, value):
        """
        Get the description and return it as a pair
        "description" : <description>
        """
        print("visiting description: ", value)
        return "description", value

    @v_args(inline=True)
    def optional(self, value):
        """
        Get the optional value and return it as a pair
        "optional" : <optional>
        """
        print("visiting optional: ", value)
        return "optional", value

    @v_args(inline=True)
    def scalar(self, value):
        print("visiting scalar: ", value)
        return value
    
    def typed_scalar(self, value):
        '''
        Receive a typed scalar in the form of a list ["!!<TYPE>"", <VALUE>]
        We extract <TYPE> from the first element and use it to find the
        corresponding constructor to coerce the type of <VALUE>
        '''
        print("visiting typed_scalar: ", value, " with type: ", value[0])
        return_value = type_constructors[value[0][2:]](value[1].value)
        return return_value
    
    @v_args(inline=True)
    def scalar_type(self, t):
        print("visiting scalar_type: ", t)
        return t
        

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False
