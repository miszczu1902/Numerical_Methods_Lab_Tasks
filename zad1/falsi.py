from horner import horner
from wykres import rysuj_wykres
import numpy as np


# a, b - krance przedzialu
# N - ilosc iteracji (jak 0 to wykonujemy do dokladnosci epsilon)
def falsi(a, b, N, wsp, len, epsilon, fa, fb):
    # fa = horner(a, wsp, len)
    # fb = horner(b, wsp, len)
    x0 = a
    x1 = b
    x = np.arange(0, 10, 0.1)
    y = horner(x, wsp, len)

    if fa * fb > 0:
        return "Funkcja nie spelnia zalozen!"
    else:
        n = 1
        while (abs(x0 - x1) > epsilon and N == 0) or (0 < n < N):
            x1 = x0
            x0 = a - (fa * (b - a) / (fb - fa))
            f0 = horner(x0, wsp, len)
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
