import numpy as np


def generate_unit_matrix(n):
    result = np.zeros((n, n))

    for i in range(n):
        result[i][i] = 1

    return result


def matrix_A(content, n):
    result = np.zeros((n, n))

    for x in range(n):
        for y in range(n):
            # result[x][y] = float(input("Podaj element " + str(x) +"," + str(y) + " macierzy A: \n"))
            result[x][y] = float(content[x][y])

    return result


def matrix_B(content, n):
    result = np.zeros(n).reshape(n, 1)

    for i in range(n):
        # result[i] = float(input("Podaj element " + str(i) + " macierzy B: \n"))
        result[i] = float(content[i][n])

    return result
