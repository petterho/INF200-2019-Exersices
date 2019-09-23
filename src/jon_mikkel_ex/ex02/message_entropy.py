from src.jon_mikkel_ex.ex01.letters_counts import letter_freq


def entropy(message):
    pass


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
