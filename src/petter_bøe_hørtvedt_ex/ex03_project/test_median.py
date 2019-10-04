# -*- coding: utf-8 -*-

__author__ = 'Petter Bøe Hørtvedt'
__email__ = 'petterho@nmbu.no'


import pytest


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sorted_data = sorted(data)
    number_of_elements = len(sorted_data)
    if number_of_elements == 0:
        raise ValueError
    else:
        if number_of_elements % 2 == 1:
            return sorted_data[number_of_elements // 2]
        else:
            return (
                    0.5 * (sorted_data[number_of_elements // 2 - 1]
                           + sorted_data[number_of_elements // 2])
            )


def test_median_single_element_list():
    """Test that the median function works for list with a single element """
    assert median([1]) == 1, 'Does not work with single element lists'


def test_median_odd_element_list():
    """Test that the median function works for lists of odd lengths"""
    assert median([3, 1, 2]) == 2, 'Does not work for lists of odd lengths'


def test_median_even_element_list():
    """Test that the median function works for lists of even lengths"""
    assert median([4, 1, 3, 2]) == 2.5, 'Does not work for lists ' \
                                        'of even lengths'


def test_median_ordered_list():
    """Test that the median function works for ordered lists"""
    assert median([1, 2, 3, 4]) == 2.5, 'Does not work for ordered lists'


def test_median_reverse_ordered_list():
    """Test that the median function works for reverse ordered lists"""
    assert median([3, 2, 1]) == 2, 'Does not work for reversed ordered lists'


def test_median_unordered_list():
    """Test that the median function works for unordered lists"""
    assert median([10, 5, 2, 7, 6]) == 6, 'Does not work for unordered list'


def test_median_empty_list():
    """Test that the median function raise ValueError if it is given an empty
     list"""
    try:
        median([])
        assert False, 'Does not raise ValueError for empty lists'
    except ValueError:
        assert True


def test_median_raises_value_error_on_empty_list():
    """Test that the median function raise ValueError if it is given an empty
     list"""
    with pytest.raises(ValueError):
        median([])


def test_median_original_data_unchanged():
    """Test that the median function leaves the original data unchanged"""
    original_data = [3, 7, 4, 2, 5]
    median(original_data)
    assert original_data == [3, 7, 4, 2, 5], 'Does change the original data'


def test_median_tuples():
    """"Test that the median function works for tuples as well as lists"""
    assert median((3, 1, 2)) == 2, 'Does not work with tuples'
