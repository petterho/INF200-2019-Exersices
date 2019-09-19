def letter_freq(txt):
    txt.lower()
    freq_dict = dict()
    for sign in txt:
        if sign in freq_dict.keys():
            freq_dict[sign] += 1
        else:
            freq_dict[sign] = 1
    return freq_dict


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
