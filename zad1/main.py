import math
import numpy as np
import PySimpleGUI as sg
from falsi import falsi
from horner import horner


wsp = [1, 2, 1, -2]
# a = -5
# b = 10
# fa = horner(a, wsp, len(wsp))
# fb = horner(b, wsp, len(wsp))
# print(falsi(-5, 10, 0, wsp, len(wsp), 0.00001, fa, fb))

wsp.clear()
tmp = []
for i in range(0, 2):
    x = int(input("Podaj x: \n"))
    tmp.append(x)
wsp = [1]
fa = horner(math.cos(tmp[0]), wsp, len(wsp))
print(fa)
fb = horner(math.cos(tmp[1]), wsp, len(wsp))
print(fb)
print(falsi(tmp[0], tmp[1], 6, wsp, len(wsp), 0.001, fa, fb))
#
#
# wsp.clear()
# tmp = []
# x2 = int(input("Podaj x2: \n"))
# for i in range(0, 2):
#     x = int(input("Podaj x: \n"))
#     tmp.append(x)
# wsp = [3]
# a=wsp**x2
# fa = horner(tmp[0], wsp, len(wsp))
# print(fa)
# fb = horner(tmp[1], wsp, len(wsp))
# print(fb)
# print(falsi(tmp[0], tmp[1], 0, wsp, len(wsp), 0.001, fa, fb))






# sg.Popup('Hello World', str(falsi(-10, 10, 0, wsp, len(wsp), 0.001, 0)))
# wsp = [2, 1]
# sg.Popup('Hello World', str(falsi(-1, 1, 0, wsp, len(wsp), 0.001, 1)))

# layout = [[sg.Text('Podaj epsilon')],
#           [sg.Input(key='_EPSILON_', size=(20, 5))],
#           [sg.Text('Podaj ilosc iteracji')],
#           [sg.Input(key="_ITER_", size=(20, 5))],
#           [sg.Button('Wylicz'), sg.Button('Zakoncz')]]
#
# window = sg.Window(title="Zadanie 1", layout=layout, margins=(400, 300)).read()
#
# while True:
#     event, values = window.read()
#     # End program if user closes window or
#     # presses the OK button
#     if event in (None, 'Zakoncz'):
#         break
#     elif event == 'Wylicz':
#         print("lol")
#         # wsp = [1, -2, -2, 3]
#         # str(falsi(-10, 10, 0, wsp, len(wsp), 0.001, 0)))
# window.Close()
