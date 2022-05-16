import numpy as np
from Value import funkcja
from laguerre import gauss, gauss_licznik, laguerre_wsp, wielomian_wsp, wielomian_wartosc
import matplotlib.pyplot as plt

amountOfNodes = 0
print(" 1. e**-x * sin(x)\n"
      " 2. e**-x * cos(x)\n"
      " 3. e**-x * x**3-x**2-2x+1\n"
      " 4. e**-x * 3**x\n"
      " 5. e**-x * |x-1|\n"
      " 6. e**-x * 2*x\n"
      " 0. wyjscie"
      )

menu = 8
while menu != 0:
    menu = int(input("wybierz wzor: \n"))

    if menu >= 1 and menu <= 6:
        a = float(input("podaj poczatek przedzialu: \n"))
        b = float(input("podaj koniec przedzialu: \n"))

        k = 0
        while k <= 1:
            k = float(input("podaj stopien wielomianu: \n"))
            if k <= 1:
                print("Stopien musi byc > 1")

        ilosc_wezlow = 0
        while ilosc_wezlow < 2 or ilosc_wezlow > 5:
            ilosc_wezlow = float(input("podaj ilosc wezlow: \n"))
            if ilosc_wezlow < 2 or ilosc_wezlow > 5:
                print("Ilosc wezlow <2;5>")

        x = np.linspace(a, b, 1000)
        tab_wsp = wielomian_wsp(menu, ilosc_wezlow, k)
        result = wielomian_wartosc(tab_wsp, k, x)

        plt.plot(x, funkcja(x, menu), label='funkcja aproksymowana')
        # epsilon = float(input("podaj dokladnosc: \n"))

        # for amountOfNodes in range(2, 6):
        #     gaussValue = round(gauss(menu, amountOfNodes), 5)  # obliczenie kwadratury Gaussa
        #     if amountOfNodes == 3:
        #         xd = 0
        #         # newtonValue = round(newton_cotes(menu, epsilon), 5)  # obliczenie kwadratury Newtona-Cotes'a
        #         # print("Liczba wezlow: ", amountOfNodes, " Gauss-Laguerre: ", gaussValue, " Newton-Cotes: ", newtonValue)
        #     else:
        #         xd = 1
        #         # print("Liczba wezlow: ", amountOfNodes, " Gauss-Laguerre: ", gaussValue)
    else:
        print("podaj liczbe z zakresu")
        menu == 8
