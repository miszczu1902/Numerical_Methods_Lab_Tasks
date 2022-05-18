from Value import funkcja
import math


def wsp(nodes, nodeNumber):
    """
    :param nodes: liczba węzłów (int)
    :param nodeNumber: numer węzła (int)
    :return: para liczb: (wartość w węźle, waga)
    """
    data = (

        ((0.585789, 0.853553), (3.414214, 0.146447)),
        ((0.415775, 0.711093), (2.294280, 0.278518), (6.289945, 0.010389)),
        ((0.322548, 0.603154), (1.745761, 0.357419), (4.536620, 0.038888), (2.395071, 0.000539)),
        ((0.263560, 0.521756), (1.413403, 0.398667), (3.596426, 0.075942), (7.085810, 0.003612), (12.640801, 0.000032))
    )
    return data[nodes - 2][nodeNumber - 1]


def gauss(func, liczba_wezlow, k):
    """
    Obliczanie całki występującej we wzorze na współczynnik wielomianu aproksymującego w liczniku
    :param wybor_funkcji: wybór dostępnej funkcji (String)
    :param amountOfNodes: liczba węzłów (int)
    :param k: stopień wielomianu aproksymującego (int)
    :return: wartość kwadratury w liczniku
    """
    calka = 0

    for i in range(liczba_wezlow):
        x = (wsp(liczba_wezlow, i)[0])
        a = (wsp(liczba_wezlow, i)[1])
        calka += a * funkcja(x, func) * laguerre(k, x)

    return calka


def licz_blad(wybor_funkcji, k, tab_wsp, liczba_wezlow):
    """
    :param wybor_funkcji: -//-
    :param k: stopień wielomianu aproksymującego (int)
    :param tab_wsp: lista współczynników wielomianu aproksymującego
    :param liczba_wezlow: liczba węzłów kwadratury (int)
    :return: wartość całki oznaczająca błąd aproksymacji
    """
    calka = 0

    for i in range(liczba_wezlow):
        x = (wsp(liczba_wezlow, i)[0])
        w = (wsp(liczba_wezlow, i)[1])
        calka += w * (funkcja(x, wybor_funkcji) - wartosc_wielomianu(k, x, tab_wsp)) ** 2

    return math.sqrt(calka)


def licz_wspolczynnik_apr(wybor_funkcji, liczba_wezlow, k):
    """
    :param wybor_funkcji: -//-
    :param liczba_wezlow: -//-
    :param k: -//-
    :return: wspołczynnik wielomianu aproksymujacego
    """
    wsp = gauss(wybor_funkcji, liczba_wezlow, k)

    return wsp / math.factorial(k) ** 2


def licz_wspolczynniki_wiel(wybor_funkcji, liczba_wezlow, k):
    """
    :param wybor_funkcji: -//-
    :param liczba_wezlow: -//-
    :param k: -//-
    :return: lista wspołczynników wielomianu aproksymującego
    """
    wielomian = []

    for i in range(k + 1):
        wielomian.append(licz_wspolczynnik_apr(wybor_funkcji, liczba_wezlow, i))

    return wielomian


def wartosc_wielomianu(k, x, tab_wsp):
    """
    :param k: -//-
    :param x: -//-
    :param tab_wsp: -//-
    :return: wartość wielomianu aproksymującego dla argumentu x
    """
    result = 0

    for i in range(k + 1):
        result += tab_wsp[i] * laguerre(i, x)

    return result


def laguerre(k, x):
    """
    :param k: stopień wielomianu (int)
    :param x: argument funkcji (float)
    :return: wartość funkcji bazowej Legendre'a dla x stopnia k
    """
    result = [1, x - 1]

    for i in range(1, k):
        result.append(((x - (2 * i) - 1) * result[i]) - ((i ** 2 * result[i - 1])))

    return result[k]
