# -*- coding: utf-8 -*-

__author__ = "Jon-Mikkel Korsvik", "Petter Bøe Hørtvedt"
__email__ = "jonkors@nmbu.no", "petterho@nmbu.no"
__version__ = "0.0.1"


from random import randint, shuffle
from random import seed as random_seed


class Board:
    """
    Handles the information about the board, including ladders, snakes,
    goal.

    Methods
    -------
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

    Methods
    -------
        dice_throw
            Returns a dice throw

        climb_or_fall
            Returns the move based on the snakes and ladders

        move
            Moves player and checks with board position
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
        else:
            self.position += dice_throw

        if self.climb_or_fall() > 0:
            self.climbed_ladder = True  # Climbed ladder, will take less steps
        self.position += self.climb_or_fall()


class Simulation:
    """
    Manages simulation of the boards and players
    """
    def __init__(self, player_field, board=None, seed=None,
                 randomize_players=True):
        self.board = board
        random_seed(seed)
        self.player_field = player_field
        self.randomize = randomize_players
        if board is None:
            self.board = Board()
        else:
            self.board = board
        self.results = []

    def single_game(self):
        num_of_turns = 0
        if self.randomize:
            shuffle(self.player_field)

        players = []
        for player in self.player_field:
            players.append(player(self.board))

        while True:
            num_of_turns += 1
            for player in players:
                player.move()
                if self.board.goal_reached(player.position):
                    return num_of_turns, type(player).__name__

    def run_simulation(self, number_of_simulations=10):
        for _ in range(number_of_simulations):
            self.results.append(self.single_game())

    def get_results(self):
        return self.results

    def winners_per_type(self):
        dict_win_per_type = {}

        for result in self.results:
            player_type = str(result[1])

            if player_type not in dict_win_per_type.keys():
                dict_win_per_type[player_type] = 1
            else:
                dict_win_per_type[player_type] += 1

        return dict_win_per_type

    def durations_per_type(self):
        dict_duration_per_type = {}

        for result in self.results:
            player_type = str(result[1])
            duration = int(result[0])

            if player_type not in dict_duration_per_type.keys():
                dict_duration_per_type[player_type] = [duration]
            else:
                dict_duration_per_type[player_type].append(duration)

        return dict_duration_per_type

    def players_per_type(self):
        dict_players_per_type = {}

        for player in self.player_field:
            player_type = str(player.__name__)

            if player_type not in dict_players_per_type.keys():
                dict_players_per_type[player_type] = 1
            else:
                dict_players_per_type[player_type] += 1

        return dict_players_per_type


if __name__ == '__main__':
    # sim = Simulation([LazyPlayer])
    # print(sim.single_game())
    board_ = Board()
    LP = LazyPlayer(board_)
    print(LP.position)
    LP.move()
    print(LP.position)
