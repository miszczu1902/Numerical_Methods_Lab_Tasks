import numpy as np


def matrix_to_gauss_jordan(matrixA, matrixB, n):
    solutionMatrix = np.zeros(n)
    mergedMatrix = np.concatenate((matrixA, matrixB), axis=1)
    rankA = np.linalg.matrix_rank(matrixA)
    rankM = np.linalg.matrix_rank(mergedMatrix)

    if rankA != rankM:
        return "Uklad sprzeczny", "!"
    if rankA == rankM and rankM < n:
        return "Uklad nieoznaczony", "!"
    else:
        for i in range(n):
            for j in range(n):
                if i != j:
                    tmp = mergedMatrix[j][i] / mergedMatrix[i][i]
                    for k in range(n + 1):
                        mergedMatrix[j][k] -= (tmp * mergedMatrix[i][k])

        for i in range(n):
            solutionMatrix[i] = mergedMatrix[i][n] / mergedMatrix[i][i]

    return mergedMatrix, solutionMatrix
