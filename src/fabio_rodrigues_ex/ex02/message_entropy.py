import math as m


def letter_freq(txt):
    """ Returns a dictionary = {(key : value)}, from the input string, with key = letters and
    value = the number of occurrences of the letter in the given string.
    """
    return dict([(i, txt.count(i)) for i in txt.lower()])


def entropy(message):
    """
    :param message:
    N: number of letters in message
    n_i: number of occurrences of letter i (i is the UTF-8 code for the letter)
    p_i = n_i/N: frequency of the letter in the message
    :return:
    The entropy calculated according to the equation H
    """
    num_letters = len(message)
    n_i = letter_freq(message)
    p_i = [n_i[i] / num_letters for i in n_i]
    return -1 * sum([p_i[i] * m.log2(p_i[i]) for i in range(len(p_i))])


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
