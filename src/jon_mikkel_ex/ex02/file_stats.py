# -*- coding: utf-8 -*-

__author__ = "Jon-Mikkel Korsvik"
__email__ = "jonkors@nmbu.no"


def char_counts(text_filename):
    """ Opens a file for reading and makes a list of each character with a
        code lower than 256, and records the occurrences
        Returns
        --------
        A list of each characters code and its occurrences
    """

    list_of_char_code_with_freq = [0 for _ in range(256)]
    with open(text_filename, 'r', encoding='utf-8') as txt:
        for line in txt:
            for char in line:
                if ord(char) < 256:
                    list_of_char_code_with_freq[ord(char)] += 1

    return list_of_char_code_with_freq


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
