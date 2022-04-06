import numpy as np
import matplotlib.pyplot as plt
from Value import Y_Value
import math
def Interpolation(x,y):
    xplt = np.linspace(x[0], x[-1])
    yplt = np.array([], float)
    for xp in xplt:
        yp=0
        for xi, yi in zip(x, y):
            yp += yi * np.prod((xp - x[x != xi]) / ((xi - x[x != xi])))
        yplt = np.append(yplt, yp)
    plt.plot(x,y,'ro',xplt,yplt,'b-')

    x3=np.array([],float)
    y3=np.array([],float)

    for i in np.arange(-5,5,0.05):
        x3=np.append(x3,i)
        y3 =np.append(y3,Y_Value(i, 1))


    plt.plot(x3,y3,'r-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    # import numpy as np
    # import matplotlib.pyplot as plt
    #
    # def Interpolation(x, y):
    #     xplt = np.linspace(x[0], x[-1])
    #
    #     yplt = np.array([], float)
    #     for xp in xplt:
    #         yp = 0
    #         for xi, yi in zip(x, y):
    #             yp += yi * np.prod((xp - x[x != xi]) / ((xi - x[x != xi])))
    #         yplt = np.append(yplt, yp)
    #     plt.plot(x, y, 'ro', xplt, yplt, 'b-')
    #     plt.xlabel('x')
    #     plt.ylabel('y')
    #     plt.show()
def wykresik(a,b,Model):
    x=np.array([],float)
    y=np.array([],float)

    for i in np.arange(a,b,0.05):
        x=np.append(x,i)
        y =np.append(y,Y_Value(i, Model))


    return x,y