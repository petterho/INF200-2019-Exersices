# -*- coding: utf-8 -*-

__author__ = "Jon-Mikkel Korsvik", "Petter Bøe Hørtvedt"
__email__ = "jonkors@nmbu.no", "petterho@nmbu.no"
__version__ = "0.0.1"


from random import randint


class Board:
    """
    Handles the information about the board, including ladders, snakes,
    goal.

    Methods:
        constructor

        goal_reached

        position_adjustment
    """
    def __init__(self, ladders=None, chutes=None, goal=None):
        if ladders is not None:
            self.ladders = ladders
        else:
            self.ladders = [(1, 40), (8, 10), (36, 52), (43, 62),
                            (49, 79), (65, 82), (68, 85)]
        if chutes is not None:
            self.chutes = chutes
        else:
            self.chutes = [(24, 5), (33, 3), (42, 30), (56, 37),
                           (64, 27), (74, 12), (87, 70)]
        if goal is not None:
            self.goal = goal
        else:
            self.goal = 90

    def goal_reached(self, position):
        """Checks if position is equal or greater than the goal

        Arguments
        ---------
        position : int

        Returns
        -------
        bool
        """
        return position >= self.goal

    def position_adjustment(self, position):
        """Adjust a players position if it lands on a ladder or a chute.

        Arguments
        ---------
        position: int

        Returns
        -------
        numbers of steps the player is to
        walk because of ladders or chutes: int
        """
        for ladder in self.ladders:
            if position == ladder[0]:
                return ladder[1] - ladder[0]
        for chute in self.chutes:
            if position == chute[0]:
                return chute[1] - chute[0]
        return 0


class Player:
    """
    __init___
    input - instance of Board

    Methods:
        move() - Moves player and checks with board position

    """
    def __init__(self, board):
        self.board = board
        self.position = 0

    def dice_throw(self):
        return randint(1, 6)

    def climb_or_fall(self):
        return self.board.position_adjustment(self.position)

    def move(self):
        """
        Moves the player according to a dice throw and updates position if it
        lands on a chute or a ladder, by calling the Board.position_adjustment.

        Returns
        -------
        None
        """
        self.position += self.dice_throw()
        self.position += self.climb_or_fall()


class ResilientPlayer(Player):
    """
    Subclass of Player
    Will take an extra step next turn if he fell down a chute.

    Overrides super().move
    """
    def __init__(self, board, extra_steps=1):
        self.extra_steps = extra_steps
        self.fell_down = False  # bool-statement, deciding to take extra step
        super().__init__(board)

    def move(self):
        self.position += self.dice_throw()
        if self.fell_down:
            self.position += self.extra_steps
            self.fell_down = False  # Resets the resilient part

        if self.climb_or_fall() < 0:
            self.fell_down = True  # Has fallen down. Will take extra step(s)
        self.position += self.climb_or_fall()


class LazyPlayer(Player):
    """
    Subclass of player
    """

    def __init__(self, board, dropped_steps=1):
        self.climbed_ladder = False
        self.dropped_steps = dropped_steps
        super().__init__(board)

    def move(self):
        dice_throw = self.dice_throw()

        if self.climbed_ladder:
            result = dice_throw - self.dropped_steps  # The dice throw compared
            if result > 0:
                self.position += result
            self.climbed_ladder = False  # Resets the laziness

        if self.climb_or_fall() > 0:
            self.climbed_ladder = True  # Climbed ladder, will take less steps
        self.position += self.climb_or_fall()


class Simulation:
    """
    Manages simulation of the boards and players
    """
    def __init__(self, player_field, board=None, seed=None,
                 randomize_players=True):
        

    def single_game(self):


    def run_simulation(self):
        pass

    def get_results(self):
        pass

    def winners_per_type(self):
        pass

    def durations_per_type(self):
        pass

    def players_per_type(self):
        pass



