from collections import OrderedDict


def letter_freq(txt):
    """Creates a dictionary from a string by lowering all characters, then going through each character one by one.
        Checks if its new to start counting that character,
        Returns
        -------
        An alphabetically sorted dictionary by using the OrderedDict from Collections
        Link - https://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key
    """
    dict_for_letters = {}
    txt = txt.lower()
    for each_character in txt:
        if each_character in dict_for_letters:
            dict_for_letters[each_character] += 1
        else:
            dict_for_letters[each_character] = 1

    return OrderedDict(sorted(dict_for_letters.items()))


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    print(frequencies)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
