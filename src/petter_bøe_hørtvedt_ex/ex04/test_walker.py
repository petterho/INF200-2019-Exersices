# -*- coding: utf-8 -*-

__author__ = 'Petter Bøe Hørtvedt'
__email__ = 'petterho@nmbu.no'


from src.petter_bøe_hørtvedt_ex.ex04.walker import Walker


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


def test_walker_walk_home():
    start_position = 0
    home_position = 0
    student = Walker(start_position, home_position)
    steps = student.walk_home()
    assert student.is_at_home()
    assert steps == 0
    assert steps == student.steps

    start_position = 0
    home_position = 10
    for i in range(10):
        student = Walker(start_position, home_position)
        assert student.walk_home() >= home_position

