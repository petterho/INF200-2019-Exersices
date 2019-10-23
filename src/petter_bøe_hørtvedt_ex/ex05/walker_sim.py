# -*- coding: utf-8 -*-

__author__ = 'Petter Bøe Hørtvedt'
__email__ = 'petterho@nmbu.no'


import random


class Walker:
    def __init__(self, start_position, home_position):
        """
        :param start_position: initial position of the walker
        :param home_position: position of the walker's home
        """
        self.position = start_position
        self.home_position = home_position
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
        if self.position == self.home_position:
            return True
        else:
            return False

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
    seed1 = 12345
    seed2 = 54321
    for i in range(2):
        print(f'Simulation from 0 to 10 and seed {seed1}:')
        sim_inst = Simulation(0, 10, seed1)
        print(sim_inst.run_simulation(20))
    print(f'Simulation from 0 to 10 and seed {seed2}:')
    sim_inst = Simulation(0, 10, seed2)
    print(sim_inst.run_simulation(20))
    for i in range(2):
        print(f'Simulation from 0 to 10 and seed {seed1}:')
        sim_inst = Simulation(10, 0, seed1)
        print(sim_inst.run_simulation(20))
    print(f'Simulation from 0 to 10 and seed {seed2}:')
    sim_inst = Simulation(10, 0, seed2)
    print(sim_inst.run_simulation(20))
