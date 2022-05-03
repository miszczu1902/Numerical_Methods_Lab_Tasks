from Value import funkcja
import numpy as np


def Simpson(a, b, numerek):
    calka = ((b - a) / 6) * (np.e ** (- a) * funkcja(a, numerek)
                             + 4 * np.e ** (- (a + b) / 2) * funkcja(((a + b) / 2), numerek)
                             + np.e ** (- b) * funkcja(b, numerek))
    return calka


def zlozonySimpson(poczatek_przedzialu, koniec_przedzialu, wybor_funkcji, eps):
    calka = Simpson(poczatek_przedzialu, koniec_przedzialu, wybor_funkcji)
    warunek = True
    n = 2
    while warunek:
        nowa_calka = 0
        h = (koniec_przedzialu - poczatek_przedzialu) / (2 * n)  # n - liczba podprzedzialow
        a = poczatek_przedzialu
        b = a + 2 * h
        for i in range(n):
            i = Simpson(a, b, wybor_funkcji)
            nowa_calka += i
            a = b
            b += 2 * h
        if abs(nowa_calka - calka) < eps:
            warunek = False
            calka = nowa_calka
        else:
            calka = nowa_calka
            n += 1  # zwiekszanie ilosci przedzialow o 1
    return calka


def newton_cotes(wybor_funkcji, eps):
    a = 0
    delta = 1
    suma = 0
    flag = True
    while flag:
        calka = zlozonySimpson(a, a + delta, wybor_funkcji, eps)
        suma += calka
        a += delta
        if abs(calka) <= abs(eps):
            flag = False
    return suma


def wsp(nodes, nodeNumber):
    data = (
        ((0.585789, 0.853553), (3.414214, 0.146447)),
        ((0.415775, 0.711093), (2.294280, 0.278518), (6.289945, 0.010389)),
        ((0.322548, 0.603154), (1.745761, 0.357419), (4.536620, 0.038888), (2.395071, 0.000539)),
        ((0.263560, 0.521756), (1.413403, 0.398667), (3.596426, 0.075942), (7.085810, 0.003612), (12.640801, 0.000032))
    )
    return data[nodes - 2][nodeNumber]


def gauss(func, amountOfNodes):
    integral = 0
    for i in range(amountOfNodes):
        x = (wsp(amountOfNodes, i)[0])
        a = (wsp(amountOfNodes, i)[1])
        integral += a * funkcja(x, func)
    return integral
