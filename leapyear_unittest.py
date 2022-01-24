# -*- coding: utf-8 -*-

import unittest
from leapyear import leapyear

test_cases = [(1, False), (4, True), (5, False),
              (8, True), (100, False), (120, True),
              (200, False), (400, True), (800, True)]


class TestTennis(unittest.TestCase):

    def test_leapyear(self):
        for testcase in test_cases:
            (year, expected_result) = testcase
            actual_result = leapyear(year)
            self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
