from uonTypes.uon_pair_key import UonPairKey, UonPairKeyProperties

# ============================== PAIR KEY TESTS ==============================


class TestUonPairKey:
    def test_pair_key_with_all_properties_representation(self):
        properties = UonPairKeyProperties("A description", True)
        uonkey = UonPairKey("A key", properties)
        assert uonkey.__repr__() == "A key (description= A description, optional= True)"

    def test_pair_key_without_properties_representation(self):
        properties = None
        uonkey = UonPairKey("A key", properties)
        assert uonkey.__repr__() == "A key"

# =========================== UON DICTIONARY TESTS ===========================


class TestUonDictionary:
    def test_uon_dict_output(self):
        # TODO
        assert "" == ""
