from random import randint

__author__ = ''
__email__ = '@nmbu.no'


def guess_input():
    guess = 0
    while guess < 1:
        guess = int(input('Your guess: '))
    return guess


def throw_dice():
    return randint(1, 6) + randint(1, 6)


def check_answer(answer, guess):
    return answer == guess


if __name__ == '__main__':

    won_game = False
    tries = 3
    correct_answer = throw_dice()
    while not won_game and tries > 0:
        players_guess = guess_input()
        won_game = check_answer(correct_answer, players_guess)
        if not won_game:
            print('Wrong, try again!')
            tries -= 1

    if tries > 0:
        print('You won {} points.'.format(tries))
    else:
        print('You lost. Correct answer: {}.'.format(correct_answer))
