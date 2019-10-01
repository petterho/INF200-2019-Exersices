# -*- coding: utf-8 -*-

__author__ = "Jon-Mikkel Korsvik"
__email__ = "jonkors@nmbu.no"

import pytest


def median(data):  # Collected from :
    # https://github.com/yngvem/INF200-2019-Exercises.git
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sorted_data = sorted(data)
    n = len(sorted_data)
    return (sorted_data[n // 2] if n % 2 == 1
            else 0.5 * (sorted_data[n // 2 - 1] + sorted_data[n // 2]))


def test_single_element_list():
    assert median([4]) == 4


def test_list_odd_number_of_elements():
    assert median([1, 2, 3, 4, 5]) == 3


def test_list_even_number_of_elements():
    assert median([1, 2, 3, 4]) == 2.5


def test_ordered_list():
    assert median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5


def test_unordered_list():
    assert median([4, 2, 3, 1]) == 2.5


def test_reversed_ordered_list():
    assert median([3, 2, 1]) == 2


