from Value import funkcja
import math


def wsp(nodes, nodeNumber):
    data = (

        ((0.585789, 0.853553), (3.414214, 0.146447)),
        ((0.415775, 0.711093), (2.294280, 0.278518), (6.289945, 0.010389)),
        ((0.322548, 0.603154), (1.745761, 0.357419), (4.536620, 0.038888), (2.395071, 0.000539)),
        ((0.263560, 0.521756), (1.413403, 0.398667), (3.596426, 0.075942), (7.085810, 0.003612), (12.640801, 0.000032))
    )
    return data[nodes - 2][nodeNumber - 1]


def gauss(func, amountOfNodes, k):
    integral = 0

    for i in range(amountOfNodes):
        x = (wsp(amountOfNodes, i)[0])
        a = (wsp(amountOfNodes, i)[1])
        integral += a * funkcja(x, func) * funkcja_bazowa(k, x)
    return integral


def gauss_blad(wybor_funkcji, k, tab_wsp, liczba_wezlow):
    calka = 0

    for i in range(liczba_wezlow):
        x = (wsp(liczba_wezlow, i)[0])
        w = (wsp(liczba_wezlow, i)[1])
        calka += w * (funkcja(x, wybor_funkcji) - wart_wielomian(k, x, tab_wsp)) ** 2

    return math.sqrt(calka)


def wsp_apro(wybor_funkcji, liczba_wezlow, k):
    wsp = gauss(wybor_funkcji, liczba_wezlow, k)
    return wsp / math.factorial(k) ** 2


def wsp_wielomian(wybor_funkcji, liczba_wezlow, k):
    wielomian = []

    for i in range(k + 1):
        wielomian.append(wsp_apro(wybor_funkcji, liczba_wezlow, i))
    return wielomian


def wart_wielomian(k, x, tab_wsp):
    result = 0

    for i in range(k + 1):
        result += tab_wsp[i] * funkcja_bazowa(i, x)
    return result


def funkcja_bazowa(k, x):
    result = [1, x - 1]

    for i in range(1, k):
        result.append(((x - (2 * i) - 1) * result[i]) - ((i ** 2 * result[i - 1])))
    return result[k]
