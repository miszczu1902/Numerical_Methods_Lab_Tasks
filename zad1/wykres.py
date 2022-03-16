import matplotlib.pyplot as plt
import numpy as np
from funkcje import f1
from funkcje import epsilonf

from mpl_toolkits.axes_grid import axislines


def ustaw_osie(x, y):
    fig = plt.figure(1)
    ax = axislines.SubplotZero(fig, 111)
    fig.add_subplot(ax)

    for direction in ['xzero', 'yzero']:
        ax.axis[direction].set_axisline_style('->', size=2)
        ax.axis[direction].set_visible(True)

    for direction in ['right', 'top', 'left', 'bottom']:
        ax.axis[direction].set_visible(False)

    ax.axis['yzero'].major_ticklabels.set_axis_direction('left')
    ax.axis['yzero'].label.set_rotation(90)
    ax.axis['yzero'].label.set_va('center')


def rysuj_wykres(x0, fx0, x, y,epsilon):
    ustaw_osie(x, y)
    a=round(max(x)/10)+1
    plt.xticks(np.arange(min(x) - 1, max(x) + 1,a))
    plt.plot(x, y)
    plt.xlim(min(x), max(x))
    plt.ylim(min(x), max(x))
    plt.scatter(x0, fx0, c="r")
    plt.text(x0, fx0+0.3, str(round(x0,epsilonf(epsilon))),fontsize=10)
    plt.text(0.06, 0.5, "x", fontsize=14, transform=plt.gcf().transFigure)
    plt.text(0.5, 0.95, "f(x)", fontsize=14, transform=plt.gcf().transFigure)
    plt.show()

def rysuj_wykres2(x, y):
    ustaw_osie(x, y)
    plt.xticks(np.arange(min(x) - 1, max(x) + 1))
    plt.plot(x, y)
    plt.xlim(min(x), max(x))
    plt.ylim(min(x), max(x))
    plt.text(0.06, 0.5, "x", fontsize=14, transform=plt.gcf().transFigure)
    plt.text(0.5, 0.95, "f(x)", fontsize=14, transform=plt.gcf().transFigure)
    plt.show()
