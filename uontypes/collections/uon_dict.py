import pprint

from uontypes.uon_value import UonValue

from binary.utils import encode_string, EOL


class UonMapping(UonValue):
    def __init__(self, mapping={}, presentation_properties={}):
        if mapping is None:
            mapping = {}
        super().__init__(mapping, "mapping", presentation_properties)

    def get(self, key):
        return self.value.get(key)

    def set_(self, key, new_value):
        self.value[key] = new_value

    def __eq__(self, other):
        if isinstance(other, UonMapping):
            return self.value == other.value
        return NotImplemented
    
    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        '''returns simple dict representation of the mapping'''
        return '{'+', '.join(
            [': '.join(map(str, k)) for k in self.value.items()])+'}'

    def __repr__(self):
        '''echoes class and reproducible representation in the REPL'''
        return 'UonMapping({})'.format(pprint.pformat(self.value))

    def to_binary(self):
        encoded_dict = b""
        for k, v in self.value.items():
            encoded_dict += (b"\x12"
                             + encode_string(k)
                             + v.to_binary())
        return b"\x02" + encoded_dict + EOL


class UonDuplicateKeyError(Exception):
    pass
