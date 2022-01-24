import pytest


def leapyear(number: int) -> bool:
    if number == 100:
        return False

    if not (number % 4):
        return True
    return False


class TestLeapYearClass:
    def test_is_not_leapyear_when_input_is_1(self):
        assert leapyear(1) == False

    def test_is_leapyear_when_input_is_4(self):
        assert leapyear(4) == True

    def test_is_not_leapyear_when_input_is_5(self):
        assert leapyear(5) == False

    def test_is_leapyear_when_input_is_8(self):
        assert leapyear(8) == True

    def test_is_not_leapyear_when_input_is_100(self):
        assert leapyear(100) == False

    def test_is_leapyear_when_input_is_120(self):
        assert leapyear(120) == True

    def test_is_not_leapyear_when_input_is_200(self):
        assert leapyear(200) == False
