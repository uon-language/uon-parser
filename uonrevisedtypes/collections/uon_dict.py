import pprint

from uonrevisedtypes.uon_base import UonBase


class UonMapping(UonBase):
    def __init__(self, mapping, presentation_properties={}):
        super().__init__(mapping, "mapping", presentation_properties)

    def __str__(self):
        '''returns simple dict representation of the mapping'''
        return pprint.pformat(self.value)

    def __repr__(self):
        '''echoes class, id, & reproducible representation in the REPL'''
        return 'UonMapping({})'.format(pprint.pformat(self.value))

    def to_binary(self):
        return b"\x00"
