# -*- coding: utf-8 -*-

__author__ = "Jon-Mikkel Korsvik"
__email__ = "jonkors@nmbu.no"


def bubble_sort(list_for_sorting):
    """ Inputs a list for sorting, and transforms it into a new "sorted_list".
        The amount of rounds is either way 1 less than the length of the list
        because of 2 objects are compared at a time.
        Remaining is defined as the range of total number of rounds minus the
        number of rounds that has been completed.
        Start with index 0 of the list and compares it with index 1, if the
        0 is more than 1 --> they switch places. This goes all the way to the
        end of the list making sure that the largest number is placed there.
        Then a new round start and places the second largest number at the -2
        index. This continues until the list is sorted in ascending order.


    :param list_for_sorting:
    :return: sorted_list,
    """
    sorted_list = list(list_for_sorting)
    number_of_rounds = len(sorted_list) - 1
    for rounds in range(number_of_rounds):
        for remaining in range(number_of_rounds - rounds):
            if sorted_list[remaining] > sorted_list[remaining+1]:
                sorted_list[remaining], sorted_list[remaining + 1] = sorted_list[remaining + 1], sorted_list[remaining]

    return sorted_list


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
