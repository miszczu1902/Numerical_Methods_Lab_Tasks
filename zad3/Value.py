import numpy as np
import math
def Y_Value(Xk,Model):
    if Model==1:
        return np.fabs(Xk)