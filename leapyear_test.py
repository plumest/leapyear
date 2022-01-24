import unittest
import pytest


def leapyear(number: int) -> bool:
    return True


class TestLeapYearClass:
    def test_leapyear_when_input_is_4(self):
        assert leapyear(4) == True
