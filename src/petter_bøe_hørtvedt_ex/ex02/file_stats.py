# -*- coding: utf-8 -*-

__author__ = 'Petter Bøe Hørtvedt'
__email__ = 'petterho@nmbu.no'


def char_counts(textfilename):
    """Opens a text-file and counts the number of occurrences each
    character in the 8 bit UTF-8 system

    Input
    textfilename: string

    Output
    char_dict: dictionary
    """
    with open(textfilename, 'r') as reader:
        char_dict = dict()
        text = reader.read()
        for char_code in range(256):
            char_dict[char_code] = text.count(chr(char_code))
    return char_dict


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
