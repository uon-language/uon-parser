import pytest

from uontypes.old.uon_pair_key import UonPairKey, UonPairKeyProperties

from uontypes.scalars.uon_string import UonString

# ============================== PAIR KEY TESTS ==============================


class TestUonString:
    def test_string_max_length(self):
        s = 'a' * 70000
        with pytest.raises(ValueError):
            UonString(s)


class TestUonPairKey:
    def test_pair_key_with_all_properties_representation(self):
        properties = UonPairKeyProperties("A description", True)
        uonkey = UonPairKey("A key", properties)
        assert uonkey.__repr__() == "A key (description= A description, optional= True)"

    def test_pair_key_without_properties_representation(self):
        properties = None
        uonkey = UonPairKey("A key", properties)
        assert uonkey.__repr__() == "A key"
