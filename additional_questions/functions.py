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
This module contains the function implementations for the selected additional questions

"""
import math
import pandas as pd

NEW_LINE = "\n"


def divisible_by_5_but_no_7(x, y):
    """List of number divisible by 5 but not by 7

    :param x: Initial number
    :param y: Last number
    :return: Returns a list of numbers between x and y that are divisible by 5 but not by 7
    """
    return [number for number in range(x, y+1) if number % 5 == 0 and number % 7 != 0]


def perfect_squares_generator(number):
    """ Perfect squares numbers less than passed number

    :param number: A passed number
    :return: Returns all perfect squares less than the passed number

    Example 1: N=30 then the generator will give 1, 4, 9, 16, 25 sequentially
    """
    for num in range(number):
        if num > 0:
            if int(math.sqrt(num)) ** 2 == num:
                yield num


def phrase_exists_in_file(phrase, filename):
    """ Search for the passed phrase in the passed text file

    :param phrase: A phrase text to find
    :param filename: A file name to be read
    :return: Returns True if the phrase is found in the document and returns False otherwise

    Note: Newline characters will not be included in the phrase.
    """
    with open("text_to_search.txt", encoding='utf-8') as file_to_search:
        content = ' '.join([line.rstrip(NEW_LINE) for line in file_to_search.readlines()])
        return content.find(phrase) != -1


def column_total_sum(csv_filename, column):
    """Compute the sum of all number in the passed column

    :param csv_filename: A comma Separated File (csv)
    :param column: A column number (zero being the left most column)
    :return: Teturn the sum of all the entries in that column

    Assume that all the entries in the CSV are numbers.
    Assume also that there are no column headers.
    For example: if the file looks like this:
     1,2,3,4
     5,6,7,8
     9,10,11,12
    The sum of column 0 will be 1 + 5 + 9 = 15 and the sum of column 2 will be 3 + 7 + 11 = 21
    """
    return pd.read_csv(csv_filename, header=None)[column].sum()
