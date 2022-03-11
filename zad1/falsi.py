from horner import horner
from wykres import rysuj_wykres
import numpy as np
from funkcje import f1, f2, f3, f4


# a, b - krance przedzialu
# N - ilosc iteracji (jak 0 to wykonujemy do dokladnosci epsilon)
def falsi(a, b, N, wsp, len, epsilon, fa, fb, x, y, sposob):

    x0 = a
    x1 = b

    if fa * fb > 0:
        return "Funkcja nie spelnia zalozen!"
    else:
        n = 1
        while (abs(x0 - x1) > epsilon and N == 0) or (0 < n < N):
        # while (abs(f1(x0, wsp, len)) > epsilon and N == 0) or (0 < n < N):
            x1 = x0
            x0 = a - (fa * (b - a) / (fb - fa))

            if sposob == 2:
                f0 = f2(x0)
            elif sposob == 3:
                f0 = f3(x0)
            elif sposob == 4:
                f0 = f4(x0)
            else:
                f0 = f1(x0, wsp, len)
            if f0 == 0:
                return x0, n
            if fa * f0 < 0:
                b = x0
                fb = f0
            else:
                a = x0
                fa = f0
            n += 1

    rysuj_wykres(x0, f0, x, y)
    return x0, n

    # pTmp = 0
    #
    # if fa * fb > 0:
    #     return "Funkcja nie spelnia zalozen!"
    # else:
    #     n = 1
    #     p = 0
    #     while (abs(p - pTmp) > epsilon and N == 0) or (0 < n < N):
    #         pTmp = p
    #         p = (a * fb - b * fa)/(fb - fa)
    #         fp = horner(p, wsp, len)
    #
    #         if fp == 0:
    #             return p, n
    #         else:
    #             n += 1
    #             if fa * fp > 0:
    #                 a = p
    #                 fa = fp
    #             else:
    #                 b = fp
    #                 fb = fp
    #
    #     return p, n

    # # fa = horner(a, wsp, len)
    # # fb = horner(b, wsp, len)
    # x0 = a
    # x1 = b
    #
    # step = 1
    # condition = True
    # while (condition and N == 0) or (0 < step < N):
    #     x2 = x0 - (x1 - x0) * fa / (fb - fa)
    #     fx2 = horner(x2, wsp, len)
    #
    #     if fa * fx2 < 0:
    #         x2Tmp = x1
    #         x1 = x2
    #     else:
    #         x2Tmp = x0
    #         x0 = x2
    #
    #     step = step + 1
    #     condition = abs(x2 - x2Tmp) > epsilon
    #

