from integrals import licz_blad, licz_wspolczynniki_wiel, wartosc_wielomianu
from Value import funkcja
import pylab as pb
import numpy as np

ilosc_wezlow = 0
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
    ilosc_wezlow = int(input("podaj liczbe wezlow: "))
    pocz = int(input("podaj poczatek przedzialu: "))
    koniec = int(input("podaj koniec przedzialu: "))

    if menu >= 1 and menu <= 6:
        if ilosc_wezlow >= 2 and ilosc_wezlow <= 5:
            if metoda == 1:
                stopien = int(input("podaj stopien wielomianu aproksymujacego: \n"))
            else:
                blad = float(input("podaj oczekiwany blad: \n"))
                stopien = 1
                tab_wsp = licz_wspolczynniki_wiel(menu, ilosc_wezlow, stopien)
                while True:
                    if licz_blad(menu, stopien, tab_wsp, ilosc_wezlow) > blad:
                        stopien += 1
                        tab_wsp = licz_wspolczynniki_wiel(menu, ilosc_wezlow, stopien)
                    else:
                        print("Stopien wielomianu: ", stopien)
                        break

            tab_wsp = licz_wspolczynniki_wiel(menu, ilosc_wezlow, stopien)
            print("Blad aproksymacji: ", licz_blad(menu, stopien, tab_wsp, ilosc_wezlow))
        else:
            print("podaj ilosc wezlow z przedzialu <2;5>")
    else:
        print("podaj liczbe z zakresu")
        menu == 8
    arg = np.linspace(pocz, koniec, 1000)
    pb.plot(arg, funkcja(arg, menu), label='funkcja aproksymowana')
    pb.plot(arg, wartosc_wielomianu(stopien, arg, tab_wsp), label='aproksymacja')
    pb.grid(True)
    pb.legend(loc='best')
    pb.show()
