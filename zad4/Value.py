import numpy as np
import horner


def funkcja(x, Model):
    if Model == 1:
        return np.sin(x)
    elif Model == 2:
        return np.cos(x)
    elif Model == 3:
        wsp = [1, -1, -2, 1]
        return horner(x, wsp, len(wsp))
    elif Model == 4:
        return 3 ** x
    elif Model == 5:
        return np.abs(x - 5)
    elif Model == 6:
        return 2 * x
