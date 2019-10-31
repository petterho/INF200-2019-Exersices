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

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):
        """
        Generate an infinite sequence of random numbers.

        Yields
        ------
        int, None
            A random number.
        """
        # This is the way i first did it
        return RandIter(self, None)

        # Also possible to something like
        # while True:
        #     self.r_n = (self.a * self.r_n) % self.m
        #     yield self.r_n


class RandIter:
    def __init__(self, random_number_generator, length):
        """

        Arguments
        ---------
        random_number_generator :
            A random number generator with a ``rand`` method that
            takes no arguments and returns a random number.
        length : int
            The number of random numbers to generate
        """
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        """
        Initialise the iterator.

        Returns
        -------
        self : RandIter

        Raises
        ------
        RuntimeError
            If iter is called twice on the same RandIter object.
        """
        if self.num_generated_numbers is not None:
            raise RuntimeError
        self.num_generated_numbers = 0
        return self

    def __next__(self):
        """
        Generate the next random number.

        Returns
        -------
        random_number : int
            A random number.

        Raises
        ------
        RuntimeError
            If the ``__next__`` method is called before ``__iter__``.
        StopIteration
            If ``self.length`` random numbers are generated.
        pass
        """
        if self.num_generated_numbers is None:
            raise RuntimeError
        if self.length is not None:
            if self.num_generated_numbers == self.length:
                raise StopIteration

        random_number = self.generator.rand()
        self.num_generated_numbers += 1
        return random_number


if __name__ == '__main__':
    random_number_generator = LCGRand(1)
    for rand in random_number_generator.random_sequence(10):
        print(rand)

    for i, rand in enumerate(random_number_generator.infinite_random_sequence()):
        print(f'The {i}-th random number is {rand}')
        if i > 98:
            break
