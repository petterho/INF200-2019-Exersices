# -*- coding: utf-8 -*-

__author__ = 'Petter Bøe Hørtvedt'
__email__ = 'petterho@nmbu.no'


import time


class LCGRand:
    """
    A class for a linear congruential generator
    """
    def __init__(self, seed=time.time()):
        """
        Initialisation

        Parameters
        ----------
        seed: float or int
            The first number used in the generator
        """
        self.a = 7**5
        self.m = 2**31 - 1
        self.r_n = seed

    def rand(self):
        """
        Generates a new sudo-random number with each call

        Returns
        -------
        self.r_n: float or int
            The sudo-random number generated
        """
        self.r_n = (self.a * self.r_n) % self.m
        return self.r_n


class ListRand:
    """
    A class that returns elements in a list.
    """
    def __init__(self, number_list):
        """
        Initialisation

        Parameters
        ----------
        number_list: list
            A list of anything
        """
        self.list = number_list
        self.index = 0

    def rand(self):
        """
        Gives the next element in the list for each call.

        Returns
        -------
        number: any
            The next element in the list
        """
        if self.index == len(self.list):
            raise RuntimeError('Index out of bound')

        number = self.list[self.index]
        self.index += 1
        return number


if __name__ == '__main__':
    print('ListRand:')
    listrand_instance = ListRand([1, 2, -1])
    for i in range(3):
        print(listrand_instance.rand())
    try:
        listrand_instance.rand()
    except RuntimeError:
        print('Here it got a RuntimeError')
    print('\nLCGRand:')
    LCGRand_instance = LCGRand()
    for i in range(10):
        print(LCGRand_instance.rand())
