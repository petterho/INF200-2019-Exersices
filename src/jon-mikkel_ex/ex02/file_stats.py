def char_counts(textfilename):
    """Opens a file for reading and makes a list of each character with a code lower than 256, and records the
        frequencies
        Returns
        --------
        A list of each charactercode and its frequency
    """

    list_of_charcode_with_freq = [0 for _ in range(256)]
    with open(textfilename, 'r', encoding='utf-8') as txt:
        for line in txt:
            for char in line:
                if ord(char) < 256:
                 list_of_charcode_with_freq[ord(char)] += 1

    return list_of_charcode_with_freq


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