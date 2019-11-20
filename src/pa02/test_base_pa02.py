# -*- coding: utf-8 -*-

"""
Minimal set of compatibility tests for PA02.
"""

__author__ = "Jon-Mikkel Korsvik", "Petter Bøe Hørtvedt"
__email__ = "jonkors@nmbu.no", "petterho@nmbu.no"
__version__ = "0.0.1"

import src.pa02.snakes_simulations as cs
import pytest


class TestBoard:
    """
    Tests for Board class.
    """

    def test_constructor_default(self):
        """Default constructor callable."""
        b = cs.Board()
        assert isinstance(b, cs.Board)

    def test_constructor_args(self):
        """Constructor with unnamed arguments callable."""
        b = cs.Board([(1, 4), (5, 16)], [(9, 2), (12, 3)], 90)
        assert isinstance(b, cs.Board)

    def test_constructor_named_args(self):
        """Constructor with kw args callable."""
        b = cs.Board(ladders=[(1, 4), (5, 16)], chutes=[(9, 2), (12, 3)],
                     goal=90)
        assert isinstance(b, cs.Board)

    def test_goal_reached(self):
        """goal_reached() callable and returns bool"""
        b = cs.Board()
        assert isinstance(b.goal_reached(1), bool)

    def test_position_adjustment(self):
        """position_adjustment callable and returns number"""
        b = cs.Board()
        assert isinstance(b.position_adjustment(1), (int, float))


class TestPlayer:
    """
    Tests for Player class.
    """

    def test_constructor(self):
        """Player can be constructed."""
        b = cs.Board()
        p = cs.Player(b)
        assert isinstance(p, cs.Player)

    def test_move(self):
        """Player has move() method."""
        b = cs.Board()
        p = cs.Player(b)
        p.move()


class TestResilientPlayer:
    def test_constructor(self):
        """ResilientPlayer can be created."""
        b = cs.Board()
        p = cs.ResilientPlayer(b, extra_steps=4)
        assert isinstance(p, cs.ResilientPlayer)
        assert isinstance(p, cs.Player)

    def test_move(self):
        """ResilientPlayer can move."""
        b = cs.Board()
        p = cs.ResilientPlayer(b)
        p.move()


class TestLazyPlayer:
    def test_constructor(self):
        """LazyPlayer can be constructed."""
        b = cs.Board()
        p = cs.LazyPlayer(b, dropped_steps=3)
        assert isinstance(p, cs.LazyPlayer)
        assert isinstance(p, cs.Player)

    def test_move(self):
        """LazyPlayer can move."""
        b = cs.Board()
        p = cs.LazyPlayer(b)
        p.move()


class TestSimulation:
    """Tests for Simulation class."""

    def test_constructor_default(self):
        """Default constructor works."""
        s = cs.Simulation([cs.Player, cs.Player])
        assert isinstance(s, cs.Simulation)

    def test_constructor_named(self):
        """Constructor with kw args works."""
        b = cs.Board()
        s = cs.Simulation(player_field=[cs.Player, cs.Player],
                          board=b, seed=123, randomize_players=True)
        assert isinstance(s, cs.Simulation)

    def test_single_game(self):
        """single_game() returns non-negative number and class name"""
        s = cs.Simulation([cs.Player, cs.Player])
        nos, wc = s.single_game()
        assert nos > 0
        assert wc == 'Player'

    def test_run_simulation(self):
        """run_simulation() can be called"""
        s = cs.Simulation([cs.Player, cs.Player])
        s.run_simulation(2)

    def test_simulation_results(self):
        """
        - Multiple calls to run_simulation() aggregate results
        - get_results() returns list of result tuples
        """
        s = cs.Simulation([cs.Player, cs.Player])
        s.run_simulation(2)
        r = s.get_results()
        assert len(r) == 2
        s.run_simulation(1)
        r = s.get_results()
        assert len(r) == 3
        assert all(s > 0 and t == 'Player' for s, t in r)

    def test_players_per_type(self):
        """player_per_type() returns dict mapping names to non-neg numbers."""
        s = cs.Simulation([cs.Player, cs.LazyPlayer, cs.ResilientPlayer])
        p = s.players_per_type()
        assert all(k in ['Player', 'LazyPlayer', 'ResilientPlayer']
                   for k in p.keys())
        assert all(v >= 0 for v in p.values())

    def test_winners_per_type(self):
        """winners_per_type() returns dict mapping names to non-neg numbers."""
        s = cs.Simulation([cs.Player, cs.LazyPlayer, cs.ResilientPlayer])
        s.run_simulation(10)
        w = s.winners_per_type()
        assert all(k in ['Player', 'LazyPlayer', 'ResilientPlayer']
                   for k in w.keys())
        assert all(v >= 0 for v in w.values())

    def test_durations_per_type(self):
        """
        durations_per_type() returns dict mapping names to list of
        non-neg numbers.
        """
        s = cs.Simulation([cs.Player, cs.LazyPlayer, cs.ResilientPlayer])
        s.run_simulation(10)
        w = s.durations_per_type()
        assert all(k in ['Player', 'LazyPlayer', 'ResilientPlayer']
                   for k in w.keys())
        assert all(len(v) >= 0 for v in w.values())
        assert all(n >= 0 for v in w.values() for n in v)


class TestOwnTests:
    def test_player_move(self):
        """ Testing: the player never go back and beyond start position = 0"""
        board = cs.Board()
        p = cs.Player(board)
        p.move()
        assert p.position > 0

    def test_resilient_player_move(self):
        """ Testing: the player never go back and beyond start position = 0"""
        board = cs.Board()
        rp = cs.ResilientPlayer(board)
        rp.move()
        assert rp.position > 0

    def test_lazy_player_move(self):
        """ Testing: the player never go back and beyond start position = 0"""
        board = cs.Board()
        lp = cs.LazyPlayer(board)
        lp.move()
        assert lp.position > 0

    def test_resilient_player_wins_more(self):
        """
        After a run with a million games with standard board and two of each
        type of player:
        {'LazyPlayer': 295179, 'Player': 344518, 'ResilientPlayer': 360303}
        """
        sim = cs.Simulation([cs.Player, cs.Player, cs.ResilientPlayer,
                             cs.ResilientPlayer, cs.LazyPlayer, cs.LazyPlayer])
        sim.run_simulation(10 ** 4)
        dict_wins = sim.winners_per_type()
        assert dict_wins['ResilientPlayer'] > dict_wins['Player']
        assert dict_wins['LazyPlayer'] < dict_wins['Player']

    def test_if_len_of_duration_is_equal_num_of_wins(self):
        s = cs.Simulation([cs.Player, cs.LazyPlayer, cs.ResilientPlayer])
        s.run_simulation(10)
        d = s.durations_per_type()
        w = s.winners_per_type()
        for key in d:
            assert len(d[key]) == w[key]

    def test_position_adjustment_ladder(self):
        board = cs.Board()
        list_of_default_ladders = [(1, 40), (8, 10), (36, 52), (43, 62),
                                   (49, 79), (65, 82), (68, 85)]

        for start, end in list_of_default_ladders:
            assert board.position_adjustment(start) == end - start
            assert board.position_adjustment(end) == 0

    def test_position_adjustment_chutes(self):
        board = cs.Board()
        list_of_default_chutes = [(24, 5), (33, 3), (42, 30), (56, 37),
                                  (64, 27), (74, 12), (87, 70)]
        for start, end in list_of_default_chutes:
            assert board.position_adjustment(start) == end - start
            assert board.position_adjustment(end) == 0

    def test_laziness_lazy_move(self):
        ladder_board = cs.Board(ladders=[(1, 40)])
        for _ in range(1000):
            lazy = cs.LazyPlayer(ladder_board)
            lazy.position = 1
            lazy.position += lazy.climb_or_fall()
            assert lazy.position == 40
            lazy.climbed_ladder = True
            before_move = lazy.position
            lazy.move()
            assert lazy.position - before_move < 6

    def test_resillience_resi_move(self):
        n = 10000
        p = 0
        chutes_board = cs.Board(ladders=[(1000, 2000)], chutes=[(42, 30)])
        for _ in range(n):
            resilient = cs.ResilientPlayer(chutes_board)
            resilient.fell_down = True
            resilient.move()
            if resilient.position > 6:
                p += 1
        assert (p/n) > (1/6.2)  # 6.2 gives some headroom for randomness
