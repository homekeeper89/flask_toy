from . import *


def test_a():
    assert 1 == 2


class TestB:
    def test_b(self):
        assert "a".upper() == "A"

    def test_c(self):
        with pytest.raises(ZeroDivisionError):
            1 / 0


# py.test "(a or B) and not c" 왜 안되지
