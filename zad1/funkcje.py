import numpy as np
from horner import horner


def f1(x, wsp, len):
    return horner(x, wsp, len)


def f2(x,):
    return np.cos(x)


def f3(x):
    return 3 ** x - 1


def f4(x):
    return np.cos(x) + x ** 3 - 1


