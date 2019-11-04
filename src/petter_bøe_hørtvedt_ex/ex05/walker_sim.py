# -*- coding: utf-8 -*-

__author__ = 'Petter Bøe Hørtvedt'
__email__ = 'petterho@nmbu.no'


import random


class Walker:
    def __init__(self, start, home):
        """
        :param start: initial position of the walker
        :param home: position of the walker's home
        """
        self.position = start
        self.home = home
        self.steps = 0

    def move(self):
        """
        Change coordinate by +1 or -1 with equal probability.
        """
        step = -1 if random.random() < 0.5 else 1
        self.position += step
        self.steps += 1

    def is_at_home(self):
        """Returns True if walker is at home position."""
        return self.position == self.home

    def get_position(self):
        """
        Returns current position.
        """
        return self.position

    def get_steps(self):
        """Returns number of steps taken by walker."""
        return self.steps

    def walk_home(self):
        """
        A method that automatically walks the student home.

        Returns
        -------
        self.steps: int
            Number of steps taken to get home.
        """
        while not self.is_at_home():
            self.move()
        return self.steps


class Simulation:
    def __init__(self, start, home, seed=None):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        """
        self.start = start
        self.home = home
        if seed is None:
            pass
        else:
            random.seed(seed)

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        student = Walker(self.start, self.home)
        return student.walk_home()

    def run_simulation(self, num_walks=20):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """
        list_of_steps = []
        for simulation in range(num_walks):
            list_of_steps.append(self.single_walk())
        return list_of_steps


if __name__ == '__main__':
    seeds = [12345, 54321]
    start_home = [(0, 10), (10, 0)]
    n_sims = 20

    for start_pos, home_pos in start_home:
        for i in range(2):
            print(f'Simulation from {start_pos} to '
                  f'{home_pos} and seed {seeds[0]}:')
            sim_inst = Simulation(start_pos, home_pos, seeds[0])
            print(sim_inst.run_simulation(n_sims))
        print(f'Simulation from {start_pos} to '
              f'{home_pos} and seed {seeds[1]}:')
        sim_inst = Simulation(start_pos, home_pos, seeds[1])
        print(sim_inst.run_simulation(n_sims))
