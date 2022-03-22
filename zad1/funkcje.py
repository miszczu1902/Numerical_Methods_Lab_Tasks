import numpy as np
from horner import horner


def f1(x, wsp, len):
    return horner(x, wsp, len)


def f2(x):
    return 2 ** x - 3


def f3(x):
    return 3 * x + np.sin(x) - np.exp(x)


def f4(x, wsp, len):
    return horner(x, wsp, len)


def f5(x):
    return np.tan(x) - 1


def f6(x):
    return 2 + np.cos(2 * x)


def f7(x):
    return np.sin(x) - np.cos(x)


def epsilonf(e):
    a = 0
    if e > 0:
        while e < 1:
            e = e * 10
            a += 1
    return a
