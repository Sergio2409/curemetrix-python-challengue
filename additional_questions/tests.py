#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------
# Copyright (c) ░s░e░r░g░i░o░v░a░l░d░e░s░2░4░0░9░
# Mail: sergiovaldes2409@gmail.com
#
# All rights reserved.
#
#
"""
Contains all unit test for the implemented functions

"""
import unittest
from functions import *


class TestAdditionalQuestions(unittest.TestCase):

    def test_divisible_by_5_but_no_7(self):
        """
        Test the function with some defined values
        """
        self.assertEqual(divisible_by_5_but_no_7(1, 10), [5, 10])
        self.assertEqual(divisible_by_5_but_no_7(1, 100),
                         [5, 10, 15, 20, 25, 30, 40, 45, 50, 55, 60, 65, 75, 80, 85, 90, 95, 100])

    def test_perfect_squares_generator(self):
        """
        Test the function with some defined values
        """
        pos = 0
        expected = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484,
                    529, 576, 625, 676, 729, 784, 841, 900, 961]
        for perfect_square in perfect_squares_generator(1000):
            self.assertEqual(expected[pos], perfect_square)
            pos += 1
        self.assertEqual(pos, len(expected))

    def test_text_search(self):
        test_cases = [
            {'phrase': 'contains built-in modules', 'result': True},
            {'phrase': 'functionality such as file', 'result': True},
            {'phrase': 'asda functionality such as file', 'result': False},
            {'phrase': ' be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming. Some of these modules are', 'result': True}
        ]
        for case in test_cases:
            self.assertEqual(phrase_exists_in_file(case['phrase'], 'text_to_search.txt'), case['result'])

    def test_column_total_sum(self):
        test_cases = [
            {'column': 0, 'result': 15},
            {'column': 1, 'result': 18},
            {'column': 2, 'result': 21},
            {'column': 3, 'result': 24},
        ]
        for case in test_cases:
            self.assertEqual(column_total_sum('data.csv', case['column']), case['result'])


if __name__ == '__main__':
    unittest.main()
