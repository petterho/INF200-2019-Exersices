# -*- coding: utf-8 -*-

__author__ = 'Petter Bøe Hørtvedt'
__email__ = 'petterho@nmbu.no'


from src.petter_bøe_hørtvedt_ex.ex04.myrand import LCGRand, ListRand


def test_lcgrand_init():
    lcgrand_instance = LCGRand()
    lcgrand_instance.a = 16807
    lcgrand_instance.m = 2**31 -1

