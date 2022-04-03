import numpy as np


def matrix_a(content, n):
    result = np.zeros((n, n))

    for x in range(n):
        for y in range(n):
            result[x][y] = float(content[x][y])

    return result


def matrix_b(content, n):
    result = np.zeros(n)

    for i in range(n):
        result[i] = float(content[i][n])

    return result
