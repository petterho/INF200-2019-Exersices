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
