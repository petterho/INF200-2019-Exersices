# -*- coding: utf-8 -*-

__author__ = 'Petter Bøe Hørtvedt'
__email__ = 'petterho@nmbu.no'


class ListRand:
    def __init__(self, number_list):
        self.list = number_list
        self.index = 0

    def rand(self):
        if self.index == len(self.list):
            raise RuntimeError('')

        number = self.list[self.index]
        self.index += 1
        return number


if __name__ == '__main__':
    listrand_instance = ListRand([1, 2, 3])
    listrand_instance.rand()
    listrand_instance.rand()
    listrand_instance.rand()