# -*- coding: utf-8 -*-

"""
Our own set of compatibility tests for PA02.
"""

__author__ = "Jon-Mikkel Korsvik", "Petter Bøe Hørtvedt"
__email__ = "jonkors@nmbu.no", "petterho@nmbu.no"
__version__ = "0.0.1"


import src.pa02.snakes_simulations as cs


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

    def test_resilience_move(self):
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

