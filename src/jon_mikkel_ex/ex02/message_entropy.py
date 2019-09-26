# -*- coding: utf-8 -*-

__author__ = "Jon-Mikkel Korsvik"
__email__ = "jonkors@nmbu.no"

from src.jon_mikkel_ex.ex01.letters_counts import letter_freq
from math import log2


def entropy(message):
    """ Calculates the message entropy in bits.
        Borrows a function that creates a dict of all characters and keeps
        track of the occurrences.
        Furthermore goes through each value of occurrences in the dictionary.
        The frequency of each character is calculated.
        The bit entropy is the negative sum of the frequencies multiplied by
        log 2 which represents bits
        ------
        input - message, a string ('xxx')

        Returns
        -------
        bit_entropy, a float (2.00000...)
    """
    freq_dict = letter_freq(message)
    length_of_message = len(message)
    bit_entropy = 0
    for occurrences in freq_dict.values():
        frequency = occurrences / length_of_message
        bit_entropy = bit_entropy - frequency * log2(frequency)
    return bit_entropy


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
