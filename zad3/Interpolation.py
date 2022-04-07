import numpy as np
import matplotlib.pyplot as plt
from Value import Y_Value
import math
def Interpolation(a,b,x,y,Model):
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

    for i in np.arange(a,b,0.05):
        x3=np.append(x3,i)
        y3 =np.append(y3,Y_Value(i, Model))


    plt.plot(x3,y3,'r-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


