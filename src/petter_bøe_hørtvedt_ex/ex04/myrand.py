# -*- coding: utf-8 -*-

__author__ = 'Petter Bøe Hørtvedt'
__email__ = 'petterho@nmbu.no'


import time


class LCGRand:
    def __init__(self, seed=time.time()):
        self.a = 7**5
        self.m = 2**31 - 1
        self.r_n = seed

    def rand(self):
        self.r_n = (self.a * self.r_n) % self.m
        return self.r_n


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
    print('ListRand:')
    listrand_instance = ListRand([1, 2, -1])
    for i in range(3):
        print(listrand_instance.rand())
    print('LCGRand')
    LCGRand_instance = LCGRand()
    for i in range(10):
        print(LCGRand_instance.rand())
