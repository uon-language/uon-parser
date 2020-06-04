from lark import Transformer

# import custom made classes
from uonTypes.uon0.uon_key import UonKey, UonKeyProperties
from uonTypes.uon0.uon_value import UonValue


class UON0TreeToPython(Transformer):
    def string(self, s):
        print("visiting string: ", s)
        (s,) = s
        return s[1:-1]

    def number(self, n):
        print("visiting number: ", n)
        (n,) = n
        return float(n)

    def word(self, s):
        print("visiting word: ", s)
        (s,) = s
        return s[0:]

    def cname(self, s):
        ''' cnames contain only valid variable names, which will serve as the dictionary keys here '''
        print("visiting cname: ", s)
        (s,) = s
        return s[0:]

    def pair(self, key_value):
        ''' Returns a tuple containing the key and its value '''
        # Here we receive a UonKey and a UonValue. To solve the dictionary keys problems, 
        # we will decompose the uonKey into its keyname, which will serve as our key in the final dictionary
        # and the key properties, will be stored as part of the value in a dictionary of its own called properties.
        # The final result will be in the form of (key, {'properties': {}, 'value':{}})
        k, v = key_value
        print("visiting pair: ", key_value, ", pair items length: ", len(key_value), end="\n")
        result_value = {}
        if (k.properties is not None):
            result_value['properties'] = k.properties
        result_value['value'] = v
        result = (k.keyname, result_value)
        print("=========== PAIR ============")
        print(result)
        print("=============================")
        return result

    def pair_key(self, key):
        print("visiting pair_key: ", key, ", pair_key items length: ", len(key), end="\n")
        if key[1] is None:
            # No key properties
            print("pair_key key: ", key[0], key[1], end='\n')
            return UonKey(key[0], {})
        return UonKey(key[0], key[1])

    def pair_value(self, value):
        print("visiting pair_value: ", value, ", pair_value items length: ", len(value), end="\n")
        return UonValue(value[0], value[1], value[2])

    def key_properties(self, properties):
        # Check if there is no properties, or by checking if the list has only None
        if not properties or all(e is None for e in properties):
            print("visiting key_properties: ", "No key_properties", end="\n")
            return {}
        else:
            # We will be receiving properties as a list of pairs
            print("visiting key_properties: ", properties, end="\n")
            return dict(properties)

    def key_property(self, property):
        print("visiting key_property", property, end='\n')
        return property[0]

    def description(self, value):
        print("visiting description: ", value, end="\n")
        return "description", value[0]

    def optional(self, value):
        print("visiting optional: ", value, end='\n')
        return "optional", value[0]

    def unit(self, value):
        print("visiting unit: ", value, end="\n")
        return dict(unit=value[0])

    def uon_type(self, value):
        print("visiting uon_type: ", value, end="\n")
        return value
        
    # pair = tuple
    # dict = dict
    seq = list

    def dict(self, items):
        print("======== DICT ==========", end='\n')
        print("visiting dict: ", items, end='\n')
        print("========================", end='\n')
        return dict(items)

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False
