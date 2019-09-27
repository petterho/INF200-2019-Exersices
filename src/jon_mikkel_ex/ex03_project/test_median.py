# -*- coding: utf-8 -*-

__author__ = "Jon-Mikkel Korsvik"
__email__ = "jonkors@nmbu.no"


def median(data):
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


if __name__ == "__main__":
    test_single_element_list()
    test_list_odd_number_of_elements()

