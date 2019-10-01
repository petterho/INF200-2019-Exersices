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
    if n < 1:  # Raising a ValueError when the list is empty
        raise ValueError
    return (sorted_data[n // 2] if n % 2 == 1
            else 0.5 * (sorted_data[n // 2 - 1] + sorted_data[n // 2]))


def test_median_single_element_list():
    assert median([4]) == 4, 'Does not work with a single element list'


def test_list_odd_number_of_elements():
    assert median([1, 2, 3, 4, 5]) == 3, 'Does not work with odd number of \
                                          elements'


def test_median_list_even_number_of_elements():
    assert median([1, 2, 3, 4]) == 2.5, 'Does not work with even number of \
                                            elements'


def test_median_ordered_list():
    assert median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5, 'Does not work with\
                                                           ordered list'


def test_median_unordered_list():
    assert median([4, 2, 3, 1]) == 2.5, 'Does not work with unordered list'


def test_median_reversed_ordered_list():
    assert median([3, 2, 1]) == 2, 'Does not work with reversed list'


def test_median_raises_value_error_on_empty_list():
    with pytest.raises(ValueError):
        median([])


def test_median_if_original_data_unchanged():
    data = [1, 2, 3]
    median(data)
    assert data == [1, 2, 3], 'Original data is changed'


def test_median_tuple():
    assert median((1, 2, 3)) == 2, 'Does not work with tuples'
