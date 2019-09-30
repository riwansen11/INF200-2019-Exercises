def char_counts(textfilename):
    """
    :param:
    1st. Opens the file with the given filename using encoding utf-8.
    2nd. Reads the entire file content into a single string.
    3rd. Counts how often each character code (0–255) occurs in the
    string.
    :return:
    The result as a list or tuple, where result[i] gives the number of
    occurrences of character code i.

    old code:
    f = open(textfilename, "r")
    content = f.read()
    f.close()
    """
    with open(textfilename, 'r') as f:
        content = f.read()

    return [content.count(i) for i in content]


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
