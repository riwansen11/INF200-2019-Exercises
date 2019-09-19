def letter_freq(txt):
    """ Returns a dictionary = {(key : value)}, from the input string, with key = letters and
    value = the number of occurrences of the letter in the given string.
    """
    return dict([(i, text.count(i)) for i in txt])


def entropy(message):
    """
    :param message:
    :return:
    the entropy calculated according to the equation above
    """
    pass


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))