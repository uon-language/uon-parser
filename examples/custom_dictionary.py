import pprint

from collections.abc import MutableMapping

#from uonrevisedtypes.uon_base import UonBase
from abc import ABC, abstractmethod

class UonBase(ABC):
    def __init__(self):
        self._presentation_properties = {}

    @property
    def presentation_properties(self):
        return self._presentation_properties

    @presentation_properties.setter
    def set_presentation_properties(self, dict_):
        self._presentation_properties = dict_

    @abstractmethod
    def to_binary(self):
        pass



class UonDictionary(MutableMapping):
    '''
    Courtesy of https://stackoverflow.com/questions/21361106/how-would-i-implement-a-dict-with-abstract-base-classes-in-python
    Mapping that works like both a dict and a mutable object, i.e.
    d = D(foo='bar')
    and 
    d.foo returns 'bar'
    '''
    # ``__init__`` method required to create instance from class.
    def __init__(self, *args, **kwargs):
        '''Use the object dict'''
        self.__dict__.update(*args, **kwargs)

    # The next five methods are requirements of the ABC.
    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__[key]

    def __delitem__(self, key):
        del self.__dict__[key]

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    # The final two methods aren't required for implementing an ABC class
    def __str__(self):
        '''returns simple dict representation of the mapping'''
        return pprint.pformat(self.__dict__)

    def __repr__(self):
        '''echoes class, id, & reproducible representation in the REPL'''
        return 'UonDictionary({})'.format(self.__dict__)

    def to_binary(self):
        return b"\x00"

    def doSomething(self):
        print("hey!")


d = UonDictionary()
d['a'] = 3
#d['doSomething'] = 4
print(d.a)
print(d.doSomething)
#print(d['doSomething'])
