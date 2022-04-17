import numpy as np
import matplotlib.pyplot as plt
from Chebysev import Chebysev
from Interpolation import Interpolation
import math
#https://www.youtube.com/watch?v=dTGqOj1NZwY
print(" 1. 2*x+1\n"
      " 2. |x|\n"
      " 3. x**3-x**2-2x+1\n"
      " 4. 3cos(x)+1\n"
      " 5. |3cos(x)+2|\n"
      " 6. |cos(x)|-3\n"
      " 0. wyjscie"
      )
# nie wiem co z ta postacia kanoniczna na co ona gdzie co jak
# dla funkcji np. wielomianu zwyklego bez trygonometrycznych i modulow wykresy sie pokrywaja 1:1?


menu=8
while menu != 0:
    menu = int(input("wybierz wzor: \n"))
    a = float(input("podaj a: \n"))
    b = float(input("podaj b: \n"))
    n = int(input("podaj n: \n"))
    if menu>0 and menu<7:
        x1, y1 = Chebysev(a, b, n, menu)
        Interpolation(a, b, x1, y1, menu)

    else:
        print("podaj liczbe z zakresu")
        menu == 8

