from Value import Y_Value
import numpy as np
def Chebysev(a,b,n,Model):
    listX=np.array([])
    listY=np.array([])
    for k in range (n):
        if a>=-1 and a<=1 and b>=-1 and b<=1:
            Xk=np.cos(np.pi*(2*k+1)/(2*n+1))
        else:
            Xk = np.cos(np.pi * (2 * k + 1) / (2 * n + 1))
            Xk=(a+b)*0.5+Xk*(b-a)*0.5
        listX=np.append(listX,Xk)
        listY=np.append(listY,Y_Value(Xk,Model))
    return listX,listY