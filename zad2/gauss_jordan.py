import numpy as np


def matrix_to_gauss_jordan(matrixA, matrixB, n):
    solutionMatrix = np.zeros(n)
    mergedMatrix = np.concatenate((matrixA, matrixB), axis=1)
    rankA = np.linalg.matrix_rank(matrixA)
    rankM = np.linalg.matrix_rank(mergedMatrix)

    if rankA != rankM:
        return "Uklad sprzeczny", "!"
    elif rankA == rankM and rankM < n:
        return "Uklad nieoznaczony", "!"
    else:
        for i in range(n):
            if mergedMatrix[i][i] == 0.0:
                return prepare_result(mergedMatrix, solutionMatrix, n)
            for j in range(n):
                if i != j:
                    tmp = float(mergedMatrix[j][i] / mergedMatrix[i][i])
                    for k in range(n + 1):
                        mergedMatrix[j][k] = float(mergedMatrix[j][k] - tmp * mergedMatrix[i][k])

    return prepare_result(mergedMatrix, solutionMatrix, n)


def prepare_result(matrix, result, n):
    for i in range(n):
        result[i] = float(matrix[i][n] / matrix[i][i])

    return result

# def make_ones(matrix, index, n):
#     for i in range(n + 1):
#         if matrix[index][index] != 1:
#             tmp = matrix[index][index]
#             for j in range(n + 1):
#                 matrix[index][j] = matrix[index][j] / tmp
#
#
# def make_zeros(matrix, indexX, indexY, n):
#     for i in range(n + 1):
#         if matrix[indexX][indexY] != 0:
#             tmp = matrix[indexX][indexY]
#             for j in range(n + 1):
#                 matrix[indexX][j] = matrix[indexX][j] - (tmp * matrix[indexY][j])

# for i in range(n):
#     for j in range(n):
#         if i != j:
#             tmp = mergedMatrix[j][i] / mergedMatrix[i][i]
#             for k in range(n + 1):
#                 mergedMatrix[j][k] = mergedMatrix[j][k] - tmp * mergedMatrix[i][k]
#
# for i in range(n):
#     solutionMatrix[i] = mergedMatrix[i][n] / mergedMatrix[i][i]





    #     for i in range(n):
    #         if mergedMatrix[i][i] == 0.0:
    #             c = 1
    #             while (i + c) < n and mergedMatrix[i + c][i] == 0:
    #                 c += 1
    #
    #             if (i + c) == n:
    #                 break
    #
    #             j = i
    #             for k in range(n + 1):
    #                 tmp = mergedMatrix[j][k]
    #                 mergedMatrix[j][k] = mergedMatrix[j + c][k]
    #                 mergedMatrix[j + c][k] = tmp
    #
    #         for j in range(n):
    #             if i != j:
    #                 tmp = mergedMatrix[j][i] / mergedMatrix[i][i]
    #
    #                 for k in range(n + 1):
    #                     mergedMatrix[j][k] = mergedMatrix[j][k] - (mergedMatrix[i][k] * tmp)
    #
    # return prepare_result(mergedMatrix, n)
