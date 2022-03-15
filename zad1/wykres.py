import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid import axislines


def ustaw_osie():
    fig = plt.figure(1)
    ax = axislines.SubplotZero(fig, 111)
    fig.add_subplot(ax)

    for direction in ['xzero', 'yzero']:
        ax.axis[direction].set_axisline_style('->', size=2)
        ax.axis[direction].set_visible(True)

    for direction in ['right', 'top', 'left', 'bottom']:
        ax.axis[direction].set_visible(False)

    ax.axis['xzero'].set_label('x')
    ax.axis['yzero'].set_label('f(x)')

    ax.axis['yzero'].major_ticklabels.set_axis_direction('right')
    ax.axis['yzero'].set_axislabel_direction('-')
    ax.axis['yzero'].label.set_rotation(90)

    ax.axis['yzero'].label.set_va('center')


def rysuj_wykres(x0, fx0, x, y):
    ustaw_osie()
    plt.xticks(np.arange(min(x) - 1, max(x) + 1))
    plt.plot(x, y)
    plt.xlim(min(x) - 1, max(x) + 1)
    plt.ylim(min(x) - 1, max(x) + 1)
    plt.scatter(x0, fx0, c="r")
    plt.show()

# def rysuj_wykres1(a, b, c, tabX, tabY):
#     x = np.linspace(0, 7, 100)
#     if c == 0:
#         y = a * x + b
#     else:
#         y = a * x ** 2 + b * np.sin(x) + c
#     plt.plot(x, y, '-b', label='y = ax')
#     plt.scatter(tabX, tabY, c='r')
#     plt.xlabel("X")
#     plt.ylabel("f(X)")
#     plt.show()
#
#
# def rysuj_wykres2(tabX, tabX2, tabY, tabFX):
#     ax = plt.axes(projection='3d')
#     ax.plot_trisurf(tabX.flatten(), tabX2.flatten(), tabFX.flatten())
#     ax.scatter(tabX, tabX2, tabY, color="r")
#     ax.set_xlabel('X1')
#     ax.set_ylabel('X2')
#     ax.set_zlabel('FX')
#     plt.show()
#
#
# def rysuj_histogram(tabX, tabY):
#     plt.hist(tabX - tabY, 50)
#     plt.xlabel("Wartosc")
#     plt.ylabel("Ilosc wystapien")
#     plt.grid(True)
#     plt.show()
