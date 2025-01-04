from random import randint
import numpy as np


def try1():
    return [(249, 64), (224, 65), (86, 191), (57, 129), (198, 245), (231, 95), (152, 128), (2, 213), (84, 12), (47, 92),
            (48, 86), (108, 50), (216, 41), (69, 70), (130, 106), (216, 197), (111, 148), (81, 129), (211, 224),
            (107, 156)]


def try2():
    return [(95, 66), (16, 17), (93, 91), (30, 78), (86, 69), (70, 1), (62, 81), (49, 27), (78, 42), (10, 55)]


def try3():
    return [(82, 59), (4, 85), (-70, 68), (-32, 27), (46, -91), (84, 67), (-65, 53), (20, 74), (-1, -82), (3, -80)]


def try4():
    return [(13, 17), (6, 7), (16, 5), (11, 1), (18, 4), (3, 13), (16, 15), (19, 11), (4, 20), (1, 13)]


def try5():
    return [(-3, 9), (-3, 7), (-1, -3), (0, -1), (8, -2), (-2, -7), (3, -7), (9, 0), (-5, 3), (2, 3), (-2, 7), (-8, 3),
            (-10, 10), (3, 3), (9, -7)]


def evenly(s, e, n):
    x_values = np.linspace(s, e, n)  # Środki sektorów na osi x
    y_values = np.linspace(s, e, n)  # Środki sektorów na osi y
    grid_points_even = [(x, y) for x in x_values for y in y_values]  # Generowanie punktów
    return grid_points_even


def halfevenly(s1, e1, s2, e2):
    x_values = np.linspace(s1, e1, e1-s1+1)  # Środki sektorów na osi x
    y_values = np.linspace(s2, e2, e2-s2+1)  # Środki sektorów na osi y
    grid_points_even = [(x, y) for x in x_values for y in y_values]  # Generowanie punktów

    return grid_points_even


def try_evenly1():
    return [(0.0, 0.0), (0.0, 10.0), (2.5, 0.0), (2.5, 10.0), (5.0, 0.0), (5.0, 10.0), (7.5, 0.0), (7.5, 10.0),
            (10.0, 0.0), (10.0, 10.0)]


def try_evenly2():
    return evenly(0.5, 9.5, 10)


def try_evenly3():
    return [(0.0, 0.0), (0.0, 10.0), (2.5, 0.0), (2.5, 10.0), (5.0, 0.0), (5.0, 10.0), (7.5, 0.0), (7.5, 10.0),
            (10.0, 0.0), (10.0, 10.0)]


def try_evenly4():
    return evenly(-9.5, 9.5, 20)


def try_evenly5():
    return evenly(-4.5, 4.5, 10)


def try_halfevenly6():
    return halfevenly(-2, 2, -2, 25)


def try_halfevenly7():
    return halfevenly(-20, 40, -3, 10)


# Funkcja zwracajaca losowy zbior punktow o zadanych parametrach
def generate_points(n=1000, maks=10 ** 9):
    return [(randint(-maks, maks), randint(-maks, maks)) for _ in range(n)]
