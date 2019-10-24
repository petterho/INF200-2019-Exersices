# -*- coding: utf-8 -*-

__author__ = 'Petter Bøe Hørtvedt'
__email__ = 'petterho@nmbu.no'


from src.petter_bøe_hørtvedt_ex.ex05.walker_sim import Walker, Simulation


class BoundedWalker(Walker):
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
        super().__init__(start, home)

    def move(self):
        Walker.move(self)
        if self.position < self.left_limit:
            self.position = self.left_limit
        if self.position > self.right_limit:
            self.position = self.right_limit


class BoundedSimulation(Simulation):
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
        self.left_limit = left_limit
        self.right_limit = right_limit
        super().__init__(start, home, seed)

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        student = BoundedWalker(
            self.start, self.home, self.left_limit, self.right_limit)
        return student.walk_home()


if __name__ == '__main__':
    start_position = 0
    home_position = 20
    left_boundarys = [0, -10, -100, -1000, -10000]
    right_boundary = 20
    walks = 20
    for left_boundary in left_boundarys:
        print(f'Left boundary: {left_boundary:8}')
        sim_ist = BoundedSimulation(start_position, home_position,
                                    left_boundary, right_boundary)
        print(sim_ist.run_simulation(walks))
