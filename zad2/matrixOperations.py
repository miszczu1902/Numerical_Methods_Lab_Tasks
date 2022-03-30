import numpy as np


def generate_unit_matrix(n):
    result = np.zeros((n, n))

    for i in range(n):
        result[i][i] = 1

    return result

def matrix_A(n):
    result = np.zeros((n, n))

    for x in range(n):
        for y in range(n):
            result[x][y] = int(input("Podaj element " + str(x) +"," + str(y) + " macierzy A: \n"))

    return result

def matrix_B(n):
    result = np.array(n)

    for i in range(n):
        result[i] = int(input("Podaj element " + str(i) + " macierzy B: \n"))

    return result