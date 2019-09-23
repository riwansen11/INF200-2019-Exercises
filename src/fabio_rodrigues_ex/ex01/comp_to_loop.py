def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    """ Returns the same list as squares_by_comp(),
    but creates the list using a for-loop.
    """
    squares = []
    for k in range(n):
        if k % 3 == 1:
            squares.append(k**2)
    return squares


# test if squares_by_comp(n) and squares_by_loop(n) returns the same results for n = 2
if __name__ == '__main__':
    if squares_by_comp(2) != squares_by_loop(2):
        print('ERROR!')
