from random import randint

__author__ = 'FABIO RODRIGUES PEREIRA'
__email__ = 'faro@nmbu.no'


def game(max_attempts):
    """It is a game where you have x-max_attempts to guess right the sum of 2 dice.
    Your score will be the x-max_attempts minus the number of mistakes you had (attempted).
    You lose the game when reach 0 score.
    """
    num_to_guess = sum_dice()

    for attempted in range(max_attempts):
        right_guess = guess_check(guessed_num(), num_to_guess)

        if not right_guess and attempted < max_attempts-1:
            print('Wrong, try again!')

        elif right_guess and attempted < max_attempts:
            print('You won {} points.'.format(score(max_attempts, attempted)))
            break

        else:
            print('You lost. Correct answer: {}.'.format(num_to_guess))
            break


def sum_dice():
    """Returns the sum of 2 rolled random dice
    """
    return randint(1, 6) + randint(1, 6)


def guessed_num():
    """Ask for the user to guess the sum of 2 rolled dices
    """
    return int(input('Guess the sum of 2 dice rolled: '))


def guess_check(guessed_number, num_to_guess):
    """Check if the guessed number is equal to the number to guess,
    then returns true or false
    """
    return guessed_number == num_to_guess


def score(max_attempts, attempted):
    """Returns the score of the game
    """
    return max_attempts - attempted


if __name__ == '__main__':
    game(max_attempts=3)
