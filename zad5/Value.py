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

