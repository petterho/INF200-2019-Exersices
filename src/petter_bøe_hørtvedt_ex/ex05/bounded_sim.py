# -*- coding: utf-8 -*-

__author__ = 'Petter Bøe Hørtvedt'
__email__ = 'petterho@nmbu.no'


from . walker_sim import Walker, Simulation
import random


class BoundedWalker:
    def __init__(self, start, home, left_limit, right_limit):
        """
        Initialise the walker

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        self.left_limit = left_limit
        self.right_limit = right_limit

    class Walker(BoundedWalker):


    


class BoundedSimulation:
    def __init__(self, start, home, left_limit, right_limit, seed=None):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        seed : int
            Random generator seed
        """
        self.start = start
        self.home = home
        self.left_limit = left_limit
        self.right_limit = right_limit
        if seed is None:
            pass
        else:
            random.seed(seed)
