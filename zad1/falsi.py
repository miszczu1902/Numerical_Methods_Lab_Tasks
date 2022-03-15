from wykres import rysuj_wykres
from funkcje import f1, f2, f3, f4, f5, f6, f7


# a, b - krance przedzialu
# N - ilosc iteracji (jak 0 to wykonujemy do dokladnosci epsilon)
def falsi(a, b,iter, wsp, len, epsilon, fa, fb, x, y, sposob):
    x0 = a
    x1 = b
    N = 0

    if fa * fb > 0:
        return "Funkcja nie spelnia zalozen!"
    else:
        N=1
        while (abs(x0 - x1) > epsilon and iter == 0) or (0 < N < iter):
            x1 = x0
            x0 = a - (fa * (b - a) / (fb - fa))

            if sposob == 2:
                f0 = f2(x0)
            elif sposob == 3:
                f0 = f3(x0)
            elif sposob == 4:
                f0 = f4(x0, wsp, len)
            elif sposob == 5:
                f0 = f5(x0)
            elif sposob == 6:
                f0 = f6(x0)
            elif sposob == 7:
                f0 = f7(x0)
            else:
                f0 = f1(x0, wsp, len)

            if f0 == 0:
                return x0, N
            if fa * f0 < 0:
                b = x0
                fb = f0
            else:
                a = x0
                fa = f0
            N += 1

    rysuj_wykres(x0, f0, x, y)
    return x0, N
