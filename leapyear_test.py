from posixpath import split
import pytest
from leapyear import leapyear
from leapyear_unittest import test_cases


class TestLeapYear:
    @pytest.mark.parametrize(["year", "expected_result"], test_cases)
    def test_is_leapyear(self, year, expected_result):
        actual_result = leapyear(year)
        assert actual_result == expected_result
