from collections.abc import MutableMapping
from uonrevisedtypes.uon_base import UonBase


class UONDictionary(UonBase, MutableMapping):
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
        return "{" + ", ".join([str(value) for value in self.values()]) + "}"

    def __repr__(self):
        '''echoes class, id, & reproducible representation in the REPL'''
        return '{}, D({})'.format(super(UONDictionary, self).__repr__(),
                                  self.__dict__)