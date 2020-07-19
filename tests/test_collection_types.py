import pytest

from uonrevisedtypes.collections.uon_dict import UonMapping
from uonrevisedtypes.collections.uon_seq import UonSeq


class TestUonMapping:

    def test_uon_mapping_constructor(self):
        u = UonMapping({'a': 1, 'b': 2})
        assert u.value == {'a': 1, 'b': 2}

    def test_uon_mapping_get(self):
        u = UonMapping({'a': 1, 'b': 2})
        assert u.get('a') == 1

    def test_uon_mapping_set(self):
        u = UonMapping({'a': 1, 'b': 2})
        u.set_("a", 3)
        assert(u.get("a") == 3)
        u.set_("c", 4)
        assert(u.get("c") == 4)
    
    def test_mapping_constructor_none(self):
        u = UonMapping(None)
        u.set_("a", 1)
        assert u.get("a") == 1
        assert UonMapping().value == {}


class TestUonSeq:
    def test_uon_seq_constructor(self):
        v = UonSeq([1, 'a', True])
        assert v.value == [1, 'a', True]

    def test_uon_seq_get(self):
        v = UonSeq([1, 'a', True])
        assert v.get(0) == 1
        assert v.get(2)
        with pytest.raises(Exception):
            v.get(3)

    def test_uon_seq_append(self):
        v = UonSeq([1, 'a', True, 2])
        assert v.get(3) == 2

    def test_uon_seq_constructor_none(self):
        assert UonSeq().value == []
        assert UonSeq(None).value == []
    