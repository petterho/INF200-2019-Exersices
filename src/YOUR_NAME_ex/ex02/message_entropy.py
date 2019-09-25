from src.YOUR_NAME_ex.ex01.letter_counts import letter_freq
from math import log2


def entropy(message):
    # Should the import be here or should it be at the top of the page?
    """Computes the entropy of message in bits
    The formula for computing the entropy is H = - sum_i (p_i * log2(p_i)),
    where p_i = n_i / N, where n_i is the occurrence of i in the message and
    N is the total number of signs in the message.

    Here variable in formula is named:
    H, bit_entropy
    N, length_message
    n_i, occurrence, found in freq_dict
    p_i, frequency

    Input:
    message: string

    Output:
    H: float
    """
    freq_dict = letter_freq(message)
    length_message = len(message)
    bit_entropy = 0
    for occurrences in freq_dict.values():
        frequency = occurrences / length_message
        bit_entropy = bit_entropy - frequency * log2(frequency)
    return bit_entropy


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
