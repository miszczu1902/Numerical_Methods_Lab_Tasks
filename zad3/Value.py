import numpy as np
from horner import horner
def Y_Value(x,Model):
    if Model==1:
        return 2*x+1
    elif Model==2:
        return np.fabs(x)
    elif Model==3:
        wsp = [1, -1, -2, 1]
        return horner(x, wsp, len(wsp))
    elif Model==4:
        return 3*np.cos(x)+1
    elif Model==5:
        return np.fabs(3*np.cos(x)+2)
    elif Model==6:
        return np.fabs(np.sin(x))+1