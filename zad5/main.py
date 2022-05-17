from integrals import gauss_blad, wsp_wielomian, wart_wielomian
from Value import funkcja
import pylab as pb
import numpy as np

amountOfNodes = 0
menu = 8

while menu != 0:
    metoda = int(input("1 - podanie stopnia \n"
                       "2 - oczekiwany blad aproksymacji \n"))
    print(" 1. x\n"
          " 2. |x-1|\n"
          " 3. x**3+4x**2-3x-5\n"
          " 4. sin(x+7)\n"
          " 0. wyjscie"
          )

    menu = int(input("wybierz wzor: \n"))
    amountOfNodes = int(input("podaj liczbe wezlow: "))

    if menu >= 1 and menu <= 6:
        if amountOfNodes >= 2 and amountOfNodes <= 5:
            if metoda == 1:
                stopien = int(input("podaj stopien wielomianu aproksymujacego: \n"))
            else:
                blad = float(input("podaj oczekiwany blad: \n"))
                stopien = 1
                tab_wsp = wsp_wielomian(menu, amountOfNodes, stopien)

                while True:
                    if gauss_blad(menu, stopien, tab_wsp, amountOfNodes) > blad:
                        stopien += 1
                        tab_wsp = wsp_wielomian(menu, amountOfNodes, stopien)
                    else:
                        print("Stopien wielomianu: ", stopien)
                        break

            tab_wsp = wsp_wielomian(menu, amountOfNodes, stopien)
            print("Blad aproksymacji: ", gauss_blad(menu, stopien, tab_wsp, amountOfNodes))
        else:
            print("podaj ilosc wezlow z przedzialu <2;5>")
    else:
        print("podaj liczbe z zakresu")
        menu == 8
    arg = np.linspace(0, 10, 1000)
    pb.plot(arg, funkcja(arg, menu), label='funkcja aproksymowana')
    pb.plot(arg, wart_wielomian(stopien, arg, tab_wsp), label='aproksymacja')
    pb.grid(True)
    pb.legend(loc='best')
    pb.show()
