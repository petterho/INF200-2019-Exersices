# -*- coding: utf-8 -*-

__author__ = 'Petter Bøe Hørtvedt'
__email__ = 'petterho@nmbu.no'


import numpy as np


def bubble_sort(unsorted_data):
    """Bubble sorts data given as input to rising order.
    Does it iterative

    Input:
    data: list, tuple

    (Output:
    data: list
    """
    sorted_data = list(unsorted_data)
    length_list = len(sorted_data)
    for length_compare in reversed(range(length_list)):
        for compare in range(length_compare):
            if sorted_data[compare] > sorted_data[compare + 1]:
                sorted_data[compare], sorted_data[compare + 1] = sorted_data[compare + 1], sorted_data[compare]
    return sorted_data


def test_empty():
    """Test that the sorting function works for empty list"""
    assert bubble_sort([]) == []


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([1]) == [1]


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    list1 = [1, 2, 3]
    list2 = bubble_sort(list1)
    assert list1 is not list2


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    bubble_sort(data)
    assert data == [3, 2, 1]


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data = [1, 2, 3]
    assert bubble_sort(data) == data


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    assert bubble_sort([4, 4, 1, 1]) == [1, 1, 4, 4]


def test_sort_random_floats():
    """Tests that sorting works on random floats between 0 and 1"""
    data = np.random.random(100)
    sorted_data = bubble_sort(data)
    for first, second in zip(sorted_data, sorted_data[1::]):
        assert first <= second


def test_sort_string():
    """Tests that sorting works on a string"""
    data_string = 'bcabac'
    sorted_data_string = ['a', 'a', 'b', 'b', 'c', 'c']
    print(bubble_sort(data_string))
    assert bubble_sort(data_string) == sorted_data_string


def test_sort_list_of_strings():
    """Tests that sorting works on a list of strings"""
    data = ['aa', 'ba', 'ab', 'bb', 'abba', 'aabb', 'baa']
    sorted_data = ['aa', 'aabb', 'ab', 'abba', 'ba', 'baa', 'bb']
    assert bubble_sort(data) == sorted_data


if __name__ == '__main__':
    test_sort_list_of_strings()
