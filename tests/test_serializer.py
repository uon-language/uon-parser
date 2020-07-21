import pytest

from serializer import python_to_uon, UonSerializerError


class TestUonSerializeBuiltInPython:
    def test_int_to_uon(self):
        i = 56789
        assert f"!int64 {i}" == python_to_uon(i)

    def test_big_int_to_uon(self):
        i = 12314189340391302761412672607
        assert f"!int64 {i}" == python_to_uon(i)

    def test_float_to_uon(self):
        f = 56789.988
        assert f"!float64 {f}" == python_to_uon(f)

    def test_str_to_uon(self):
        s = "hello world"
        assert f"!str {s}" == python_to_uon(s)

    def test_dict_to_uon(self):
        d = {"a": 1, "nested": {"b": 2, "c": 3}}
        assert ("{a: !int64 1, nested: {b: !int64 2, c: !int64 3}}"
                == python_to_uon(d))

    def test_dict_with_invalid_keys(self):
        d = {1: 1, 2: 2}
        with pytest.raises(UonSerializerError):
            python_to_uon(d)

    def test_seq_to_uon(self):
        l = [1, 2, "3"]
        assert ("[!int64 1, !int64 2, !str 3]" == python_to_uon(l)) 
