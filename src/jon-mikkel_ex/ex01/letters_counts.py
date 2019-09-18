def letter_freq(txt):
    """Creates a """
    dict_for_letters: {}
    txt.lower()
    for each_character in txt:
        if each_character in dict_for_letters:
            dict_for_letters[each_character] += 1
        else:
            dict_for_letters[each_character] = 1

    return dict_for_letters


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))