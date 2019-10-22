# -*- coding: utf-8 -*-

__author__ = 'Petter Bøe Hørtvedt'
__email__ = 'petterho@nmbu.no'


import random


class Walker:
    def __init__(self, start_position, home_position):
        self.start_position = start_position
        self.home_position = home_position

    def move(self):
        raise NotImplementedError

    def is_at_home(self):
        raise NotImplementedError

    def get_position(self):
        raise NotImplementedError

    def get_steps(self):
        raise NotImplementedError
