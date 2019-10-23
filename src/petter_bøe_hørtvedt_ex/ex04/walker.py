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
        return step

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


if __name__ == '__main__':
    distances_home = [1, 2, 5, 10, 20, 50, 100]
    for distance in distances_home:
        steps_list = []
        for students in range(5):
            student = Walker(0, distance)
            steps_list.append(student.walk_home())
        print(f'Distance:{distance:4} Path lengths: {steps_list}')
