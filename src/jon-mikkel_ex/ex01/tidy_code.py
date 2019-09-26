from random import randint

__author__ = 'Jon-Mikkel Korsvik'
__email__ = 'jonkors@nmbu.no'


def guess_input():
    return int(input('Your guess: '))


def double_dice_throw():
    return randint(1, 6) + randint(1, 6)


def winning_state(dice, guessed):
    return dice == guessed


if __name__ == '__main__':

    game_won = False
    number_of_tries = 3
    dice_result = double_dice_throw()
    while not game_won and number_of_tries > 0:
        guess = guess_input()
        game_won = winning_state(dice_result, guess)
        if not game_won:
            print('Wrong, try again!')
            number_of_tries -= 1

    if number_of_tries > 0:
        print('You won {} points.'.format(number_of_tries))
    else:
        print('You lost. Correct answer: {}.'.format(dice_result))
