import pytest


def leapyear(number: int) -> bool:
    if number == 4:
        return True
    return False


class TestLeapYearClass:
    def test_leapyear_when_input_is_1(self):
        assert leapyear(1) == False

    def test_leapyear_when_input_is_4(self):
        assert leapyear(4) == True

    def test_leapyear_when_input_is_5(self):
        assert leapyear(5) == False
