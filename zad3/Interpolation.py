import numpy as np
import matplotlib.pyplot as plt
from Value import Y_Value
def Interpolation(a,b,x,y,Model):
    xplt = np.linspace(x[0], x[-1])
    yplt = np.array([])
    for xp in xplt:
        yp=0
        for xi, yi in zip(x, y):
            yp += yi * np.prod((xp - x[x != xi]) / ((xi - x[x != xi])))
        yplt = np.append(yplt, yp)
    plt.plot(xplt,yplt,'b-',label="Wielomian interpolacyjny")
    plt.plot(x,y,'ro',label="Wezly")

    x3=np.array([])
    y3=np.array([])

    for i in np.arange(a,b,0.05):
        x3=np.append(x3,i)
        y3 =np.append(y3,Y_Value(i, Model))

    plt.plot(x3, y3, 'r-',label="Funkcja oryginalna")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1,prop={'size': 5})
    plt.show()


