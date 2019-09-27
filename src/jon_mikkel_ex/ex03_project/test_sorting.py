# -*- coding: utf-8 -*-

__author__ = "Jon-Mikkel Korsvik"
__email__ = "jonkors@nmbu.no"

from src.jon_mikkel_ex.ex02.bubble_sort import bubble_sort
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


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    data = []
    for i in range(1000):  # Testing integers
        data.append(random.randint(1, 1000))

    new_data = bubble_sort(data)

    for index in range(len(new_data)-1):
        assert new_data[index] <= new_data[index+1]

    data = np.random.random(100)  # Testing floats
    new_data = bubble_sort(data)

    for index in range(len(new_data)-1):
        assert new_data[index] <= new_data[index+1]

    list_of_strings = ('aaa', 'bb', 'ii', 'qwr')
    bubble_sort(list_of_strings)



if __name__ == "__main__":
    test_empty()
    test_original_unchanged()
    test_single()
    test_sort_all_equal()
    test_sort_reversed()
    test_sort_sorted()
    test_sorted_is_not_original()
    test_sorting()
