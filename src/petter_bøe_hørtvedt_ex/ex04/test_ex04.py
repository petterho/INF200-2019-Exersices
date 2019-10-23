# -*- coding: utf-8 -*-

"""
Acceptance test suite for EX04.

Your code should pass these tests before submission.
"""

import pytest
from src.petter_bøe_hørtvedt_ex.ex04.myrand import LCGRand, ListRand
from src.petter_bøe_hørtvedt_ex.ex04.walker import Walker

__author__ = 'Hans Ekkehard Plesser'
__email__ = 'hans.ekkehard.plesser@nmbu.no'


def test_lcg():
    """Test that LCG generator works."""

    lcg = LCGRand(346)
    assert lcg.rand() == 5815222
    assert lcg.rand() == 1099672039


def test_list_rng():
    """Test that ListRNG generator works."""
    numbers = [4, 5, 29, 11]
    lr = ListRand(numbers)
    assert [lr.rand() for _ in range(len(numbers))] == numbers
    with pytest.raises(RuntimeError):
        lr.rand()


def test_walker():
    """Test that Walker class can be used as required."""

    start, home = 10, 20
    w = Walker(start, home)
    assert not w.is_at_home()
    w.move()
    assert w.get_position() != start
    w.move()
    assert w.get_steps() == 2


# Here are my own tests for myrand and walker
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


def test_walker_init():
    start_position = 0
    home_position = 1
    student = Walker(start_position, home_position)
    assert student.steps == 0, 'Does not assign the right variables'
    assert student.home_position == 1, 'Does not assign the right variables'
    assert student.position == 0, 'Does not assign the right variables'


def test_walker_move():
    start_position = 0
    home_position = 1
    student = Walker(start_position, home_position)
    move = student.move()
    assert student.steps == 1
    assert type(move) == int
    assert move == -1 or 1


def test_walker_move_random():
    """
    Note: This test might fail due to the randomness, but with a large number
    of steps it should not.
    """
    start_position = 0
    home_position = 1
    student = Walker(start_position, home_position)
    steps = 0
    number_of_steps = 10000
    for i in range(number_of_steps):
        steps += student.move()
    assert steps < (number_of_steps/10)
    assert steps > -(number_of_steps/10)


def test_walker_is_at_home():
    start_position = 0
    home_position = 0
    student = Walker(start_position, home_position)
    assert student.is_at_home() is True

    start_position = 0
    home_position = 1
    student = Walker(start_position, home_position)
    assert student.is_at_home() is False


def test_walker_get_position():
    start_position = 0
    home_position = 0
    student = Walker(start_position, home_position)
    assert student.get_position() == start_position


def test_walker_get_steps():
    start_position = 0
    home_position = 0
    student = Walker(start_position, home_position)
    assert student.get_steps() == 0
