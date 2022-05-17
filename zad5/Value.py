import math

import numpy as np
from horner import horner


def funkcja(x, Model):
    if Model == 1:
        return x
    elif Model == 2:
        return np.abs(x-1)
    elif Model == 3:
        wsp = [1, 4, -3, -5]
        return horner(x, wsp, len(wsp))
    elif Model == 4:
        return np.sin(x+7)
    #     if Model == 1:
    #     return np.abs(x)
    # elif Model == 2:
    #     return x+4
    # elif Model == 3:
    #     wsp = [2, -4, -8, -3]
    #     return horner(x, wsp, len(wsp))
    # elif Model == 4:
    #     return np.cos(x)

