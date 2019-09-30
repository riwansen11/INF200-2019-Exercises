def letter_freq(txt):
    """ Returns a dictionary = {(key : value)}, 
    from the input string, with key = letters and
    value = the number of occurrences of the letter 
    in the given string.
    letters = [i for i in text]
    counter = [text.count(a) for a in text]
    return dict(zip(letters, counter))
    """
    return dict([(i, txt.count(i)) for i in txt])


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')
    frequencies = letter_freq(text)

    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
