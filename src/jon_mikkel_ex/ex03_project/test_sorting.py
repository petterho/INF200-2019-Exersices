# -*- coding: utf-8 -*-

__author__ = "Jon-Mikkel Korsvik"
__email__ = "jonkors@nmbu.no"

from src.jon_mikkel_ex import bubble_sort
import random
import numpy as np


def test_empty():
    """Test that the sorting function works for empty list"""
    assert bubble_sort([]) == []


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([1]) == [1]


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    data = [3, 2, 1]
    assert bubble_sort(data) is not data


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data =
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    bubble_sort(data)
    assert data == [3, 2, 1]
    pass


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    assert bubble_sort([1, 5, 3, 2, 3, 4, 1]) == [1, 1, 2, 3, 3, 4, 5]


""" The code underneath was a part of test_sorting, but I decided that
    it would be easier to identify a failed test if they were separated.
"""


def test_integer():
    data = []
    for i in range(1000):  # Testing integers
        data.append(random.randint(1, 1000))

    new_data = bubble_sort(data)

    for index in range(len(new_data)-1):
        assert new_data[index] <= new_data[index+1]


def test_floats():
    data = np.random.random(100)  # Testing floats
    new_data = bubble_sort(data)

    for index in range(len(new_data)-1):
        assert new_data[index] <= new_data[index+1]


def test_single_string():
    string_for_test = 'afdebc'
    assert bubble_sort(string_for_test) == ['a', 'b', 'c', 'd', 'e', 'f']


def test_list_of_strings():
    list_of_strings = ('aaa', 'ii', 'bb', 'qwr')
    assert bubble_sort(list_of_strings) == ['aaa', 'bb', 'ii', 'qwr']


if __name__ == "__main__":
    test_empty()
    test_original_unchanged()
    test_single()
    test_sort_all_equal()
    test_sort_reversed()
    test_sort_sorted()
    test_sorted_is_not_original()
    test_single_string()
    test_floats()
    test_integer()
    test_list_of_strings()
