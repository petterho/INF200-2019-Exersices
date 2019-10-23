# -*- coding: utf-8 -*-

__author__ = 'Petter Bøe Hørtvedt'
__email__ = 'petterho@nmbu.no'


from src.petter_bøe_hørtvedt_ex.ex04.myrand import LCGRand, ListRand


def test_lcgrand_init():
    seed = 1000
    lcgrand_instance = LCGRand(seed)
    assert lcgrand_instance.a == 16807
    assert lcgrand_instance.m == 2**31 - 1
    assert lcgrand_instance.r_n == seed


def test_lcgrand_rand():
    """
    This test might fail due to randomness, checking that every new number
    does not equal the last. But if it fails it has reach a point where
    every number equals the last and the code has failed.
    Returns
    -------

    """
    lcgrand_instance = LCGRand()
    last_number = 0.1
    for i in range(100):
        new_number = lcgrand_instance.rand()
        assert new_number != last_number
        assert new_number < lcgrand_instance.m, \
            'The random number is not less than the modulus number'
        last_number = new_number


def test_listrand_init():
    not_so_random_list = [1, 2, 3]
    not_so_random_generator = ListRand(not_so_random_list)
    assert not_so_random_generator.list == not_so_random_list
    assert not_so_random_generator.index == 0

def test_listrand_rand():
    not_so_random_list = [1]
    not_so_random_generator = ListRand(not_so_random_list)
    assert not_so_random_generator.rand() == not_so_random_list[0]
    assert not_so_random_generator.index == 1
    try:
        not_so_random_generator.rand()
        assert False
    except RuntimeError:
        assert True



