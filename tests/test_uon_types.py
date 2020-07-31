import pytest

from uontypes.scalars.uon_string import UonString

# ============================== PAIR KEY TESTS ==============================


class TestUonString:
    def test_string_max_length(self):
        s = 'a' * 70000
        with pytest.raises(ValueError):
            UonString(s)
