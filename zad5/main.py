from integrals import gauss_blad, wsp_wielomian, wart_wielomian
from Value import funkcja
import pylab as pb
import numpy as np

amountOfNodes = 0
print(" 1. x\n"
      " 2. |x-1|\n"
      " 3. x**3+4x**2-3x-5\n"
      " 4. sin(x+7)\n"
      " 0. wyjscie"
      )


menu = 8
while menu != 0:
    menu = int(input("wybierz wzor: \n"))
    amountOfNodes = int(input("podaj liczbe wezlow: "))
    stopien = int(input("podaj stopien wielomianu aproksymujacego: \n"))
    #poczatek = int(input("podaj poczatek przedzialu: \n"))
    #koniec = int(input("podaj koniec przedzialu: \n"))
    if menu >= 1 and menu <= 6:
        # epsilon = float(input("podaj dokladnosc: \n"))
        if amountOfNodes >= 2 and amountOfNodes <= 5:
            # blad = abs(float(input("Podaj oczekiwany maksymaly blad aproksyma
            # dokladnosc = True
            # while dokladnosc:
            #     tab_wsp = wsp_wielomian(menu, amountOfNodes, stopien_apro)
            #     if gauss_blad(menu, stopien_apro, tab_wsp, amountOfNodes) < blad:
            #         dokladnosc = False
            #     else:
            #         stopien_apro += 1
            # print("Blad aproksymacji: {}".format(gauss_blad(menu, stopien_apro, tab_wsp, amountOfNodes)))
            tab_wsp = wsp_wielomian(menu, amountOfNodes, stopien)
            print("Blad aproksymacji: ", gauss_blad(menu, stopien, tab_wsp, amountOfNodes))
        else:
            print("podaj ilosc wezlow z przedzialu <2;5>")
    else:
        print("podaj liczbe z zakresu")
        menu == 8
    #arg = np.linspace(poczatek, koniec, 1000)
    arg = np.linspace(0, 10, 1000)
    pb.plot(arg, funkcja(arg, menu), label='funkcja aproksymowana')
    pb.plot(arg, wart_wielomian(stopien, arg, tab_wsp), label='aproksymacja')
    pb.grid(True)
    pb.legend(loc='best')
    pb.show()
