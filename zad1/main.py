import numpy as np
from falsi import falsi
from horner import horner
from funkcje import f1, f2, f3, f4, f5, f6, f7
from wykres import rysuj_wykres2

exit = False
menu = 8
menuStart = 8
while menuStart != 0:

    menu = 8
    print("1. wyswietl liste wzorow do wyswietlenia pelnych wykresow\n"
          "2. wyswietl liste wzorow do wyswietlenia wykresow po zastosowaniu reguly falsi\n"
          "0. wyjscie")
    menuStart = int(input("wybierz opcje: \n"))
    if menuStart == 0 or menuStart == 1 or menuStart == 2:
        if menuStart == 1:
            while menu != 0:
                print(" 1. x**3-x**2-2x+1=0\n"
                      " 2. 2**x-3x=0\n"
                      " 3. 3x+sin(x)-e**x=0\n"
                      " 4. x**3-x+1=0\n"
                      " 5. tg(x)-1=0\n"
                      " 6. 2+cos(2x)=0\n"
                      " 7. sin(x)-cos(x)=0\n"
                      " 0. wyjscie"
                      )
                menu = int(input("wybierz wzor: \n"))
                tmp = []
                wsp = []
                x = np.linspace(-5, 5, 1000)
                if menu == 1:
                    # f1
                    wsp = [1, -1, -2, 1]
                    y = horner(x, wsp, len(wsp))
                    rysuj_wykres2(x, y)

                elif menu == 2:
                    # f2
                    y = f2(x)
                    rysuj_wykres2(x, y)

                elif menu == 3:
                    # f3
                    y = f3(x)
                    rysuj_wykres2(x, y)

                elif menu == 4:
                    # f4
                    wsp = [1, 0, -1, 1]
                    y = f4(x, wsp, len(wsp))
                    rysuj_wykres2(x, y)

                elif menu == 5:
                    # f5
                    y = f5(x)
                    rysuj_wykres2(x, y)

                elif menu == 6:
                    # f6
                    y = f6(x)
                    rysuj_wykres2(x, y)

                elif menu == 7:
                    # f7
                    y = f7(x)
                    rysuj_wykres2(x, y)
                else:
                    print("podaj liczbe z zakresu")
                    menu == 8

        if menuStart == 2:
            while menu != 0:
                print(" 1. x**3-x**2-2x+1=0\n"
                      " 2. 2**x-3x=0\n"
                      " 3. 3x+sin(x)-e**x=0\n"
                      " 4. x**3-x+1=0\n"
                      " 5. tg(x)-1=0\n"
                      " 6. 2+cos(2x)=0\n"
                      " 7. sin(x)-cos(x)=0\n"
                      " 0. wyjscie"
                      )

                menu = int(input("wybierz wzor: \n"))
                tmp = []
                wsp = []
                if menu != 0 and menu > 0 and menu < 8:
                    for i in range(0, 2):
                        x = float(input("Podaj x: \n"))
                        tmp.append(x)
                    epsilon = float(input("podaj wartosc epsilon: \n"))
                    iter = 0

                    x = np.linspace(tmp[0], tmp[1], 1000)
                    if epsilon == 0:
                        iter = int(input("Podaj ilosc iteracji: \n"))

                    if menu == 1:
                        # f1
                        wsp = [1, -1, -2, 1]
                        fa = f1(tmp[0], wsp, len(wsp))
                        fb = f1(tmp[1], wsp, len(wsp))
                        y = horner(x, wsp, len(wsp))
                        print(falsi(tmp[0], tmp[1], iter, wsp, len(wsp), epsilon, fa, fb, x, y, 1))

                    elif menu == 2:
                        # f2
                        fa = f2(tmp[0])
                        fb = f2(tmp[1])
                        y = f2(x)
                        print(falsi(tmp[0], tmp[1], iter, wsp, len(wsp), epsilon, fa, fb, x, y, 2))

                    elif menu == 3:
                        # f3
                        fa = f3(tmp[0])
                        fb = f3(tmp[1])
                        y = f3(x)
                        print(falsi(tmp[0], tmp[1], iter, wsp, len(wsp), epsilon, fa, fb, x, y, 3))

                    elif menu == 4:
                        # f4
                        wsp = [1, 0, -1, 1]
                        fa = f4(tmp[0], wsp, len(wsp))
                        fb = f4(tmp[1], wsp, len(wsp))
                        y = f4(x, wsp, len(wsp))
                        print(falsi(tmp[0], tmp[1], iter, wsp, len(wsp), epsilon, fa, fb, x, y, 4))

                    elif menu == 5:
                        # f5
                        fa = f5(tmp[0])
                        fb = f5(tmp[1])
                        y = f5(x)
                        print(falsi(tmp[0], tmp[1], iter, wsp, len(wsp), epsilon, fa, fb, x, y, 5))

                    elif menu == 6:
                        # f6
                        fa = f6(tmp[0])
                        fb = f6(tmp[1])
                        y = f6(x)
                        print(falsi(tmp[0], tmp[1], iter, wsp, len(wsp), epsilon, fa, fb, x, y, 6))

                    elif menu == 7:
                        # f7
                        fa = f7(tmp[0])
                        fb = f7(tmp[1])
                        y = f7(x)
                        print(falsi(tmp[0], tmp[1], iter, wsp, len(wsp), epsilon, fa, fb, x, y, 7))
                    else:
                        print("podaj liczbe z zakresu")
                        menu == 8

                    tmp.clear()
                    wsp.clear()
                else:
                    print("podaj numer z zakresu")
