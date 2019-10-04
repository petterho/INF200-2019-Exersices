# -*- coding: utf-8 -*-

__author__ = 'Petter Bøe Hørtvedt'
__email__ = 'petterho@nmbu.no'


def bubble_sort(unsorted_data):
    """Bubble sorts data given as input to rising order.
    Does it iterative

    Input:
    data: list, tuple

    Output:
    data: list
    """
    sorted_data = list(unsorted_data)
    length_list = len(sorted_data)
    for length_compare in reversed(range(length_list)):
        for compare in range(length_compare):
            if sorted_data[compare] > sorted_data[compare + 1]:
                sorted_data[compare], sorted_data[compare + 1] = sorted_data[compare + 1], sorted_data[compare]
    return sorted_data


if __name__ == "__main__":
    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
