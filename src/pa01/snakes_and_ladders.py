# -*- coding: utf-8 -*-

__author__ = "Jon-Mikkel Korsvik", "Petter Bøe Hørtvedt"
__email__ = "jonkors@nmbu.no", "petterho@nmbu.no"
__version__ = "0.0.1"


from random import randint
from random import seed as random_seed
import numpy as np


def check_if_snake_or_ladder(position):
    """
    Tuple
    First argument: position
    Second argument: the position it leads to.
    :param position:
    :return: new position if the position is in the list of snakes and ladders:
    :if not: original position is returned
    """
    list_of_snakes_and_ladders = [
        (1, 40), (8, 10), (36, 52), (43, 62), (49, 79), (65, 82), (68, 85),
        (24, 5), (33, 3), (42, 30), (56, 37), (64, 27), (74, 12), (87, 70)]
    for start_position, end_position in list_of_snakes_and_ladders:
        if position == start_position:
            return end_position

    return position


def single_game(num_players):
    """
    Returns duration of single game.

    Arguments
    ---------
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : int
        Number of moves the winning player needed to reach the goal
    """
    num_moves = 0
    list_of_positions = [0]*num_players  # Creates a list with appropriate 0's

    while all([element < 90 for element in list_of_positions]):
        for player in range(num_players):
            list_of_positions[player] += randint(1, 6)
            cur_position = list_of_positions[player]
            list_of_positions[player] = check_if_snake_or_ladder(cur_position)
        num_moves += 1

    return num_moves


def multiple_games(num_games, num_players):
    """
    Returns durations of a number of games.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : list
        List with the number of moves needed in each game.
    """
    num_moves = []
    for game in range(num_games):
        num_moves.append(single_game(num_players))
    return num_moves


def multi_game_experiment(num_games, num_players, seed):
    """
    Returns durations of a number of games when playing with given seed.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game
    seed : int
        Seed used to initialise the random number generator

    Returns
    -------
    num_moves : list
        List with the number of moves needed in each game.
    """
    random_seed(seed)
    return multiple_games(num_games, num_players)


if __name__ == "__main__":
    array = multi_game_experiment(100, 4, 0)
    print(f'Here are some of the stats for the snakes and ladder experiment:\n'
          f'The shortest game: {np.min(array)} moves\n'
          f'The longest game: {np.max(array)} moves\n'
          f'The median game duration: {np.median(array)} moves\n'
          f'The mean game duration: {np.mean(array)} moves\n'
          f'The standard deviation: {np.std(array)} moves')
