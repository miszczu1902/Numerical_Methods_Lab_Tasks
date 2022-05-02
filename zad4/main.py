from integrals import newton_cotes,gauss
amountOfNodes = 0
print(" 1. e**-x * sin(x)\n"
      " 2. e**-x * cos(x)\n"
      " 3. e**-x * x**3-x**2-2x+1\n"
      " 4. e**-x * 3**x\n"
      " 5. e**-x * |x-1|\n"
      " 6. e**-x * 2*x\n"
      " 0. wyjscie"
      )

menu=8
while menu != 0:
    menu = int(input("wybierz wzor: \n"))

    if menu >= 1 and menu<=6:
        epsilon = float(input("podaj dokladnosc: \n"))
        newtonResult = round(newton_cotes(menu, 1e-8), 8)

        for amountOfNodes in range(2, 6):
            gaussValue = round(gauss(menu, amountOfNodes), 5)   # obliczenie kwadratury Gaussa
            if amountOfNodes == 3:
                newtonValue = round(newton_cotes(menu, epsilon), 5)   # obliczenie kwadratury Newtona-Cotes'a
                print("Liczba wezlow: ", amountOfNodes," Gauss-Laguerre: ", gaussValue, " Newton-Cotes: ", newtonValue)
            else:
                print("Liczba wezlow: ", amountOfNodes, " Gauss-Laguerre: ", gaussValue)
    else:
        print("podaj liczbe z zakresu")
        menu == 8





#
#
# from integrals import newton_cotes,gauss
# amountOfNodes = 0
# print(" 1. e**-x * sin(x)\n"
#       " 2. e**-x * cos(x)\n"
#       " 3. e**-x * x**3-x**2-2x+1\n"
#       " 4. e**-x * 3**x\n"
#       " 5. e**-x * |x-1|\n"
#       " 6. e**-x * 2*x\n"
#       " 0. wyjscie"
#       )
#
# menu=8
# while menu != 0:
#     menu = int(input("wybierz wzor: \n"))
#
#     if menu >= 1 and menu<=6:
#         epsilon = float(input("podaj dokladnosc: \n"))
#         newtonResult = round(newton_cotes(menu, epsilon), 8)
#
#         for amountOfNodes in range(2, 6):
#             gaussValue = round(gauss(menu, amountOfNodes), 5)   # obliczenie kwadratury Gaussa
#             if amountOfNodes == 3:
#                 newtonValue = round(newton_cotes(menu, epsilon), 5)   # obliczenie kwadratury Newtona-Cotes'a
#                 print("Liczba wezlow: ", amountOfNodes," Gauss-Laguerre: ", gaussValue, " Blad (%) Gauss-Laugerre: ",
#                       round(abs((gaussValue - newtonResult) / newtonResult * 100), 2), " Newton-Cotes: ", newtonValue, " Blad (%) Newton-Cotes: ",
#                       round(abs((newtonValue - newtonResult) / newtonResult * 100), 2))
#             else:
#                 print("Liczba wezlow: ", amountOfNodes, " Gauss-Laguerre: ", gaussValue, " Blad (%) Gauss-Laugerre: ",
#                       round(abs((gaussValue - newtonResult) / newtonResult * 100), 2), "")
#     else:
#         print("podaj liczbe z zakresu")
#         menu == 8
#
#
#
#
#
#
#
#
#
#
