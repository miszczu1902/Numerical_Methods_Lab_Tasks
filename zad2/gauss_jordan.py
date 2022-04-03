import numpy as np


def matrix_to_gauss_jordan(matrixA, matrixB, n):
    # przygotowanie macierzy
    matrixBTmp = np.array(matrixB).reshape(n, 1)
    mergedMatrix = np.concatenate((matrixA, matrixBTmp), axis=1)

    # liczymy rzad dla: pierwotnej i nowej macierzy
    rankA = np.linalg.matrix_rank(matrixA)
    rankM = np.linalg.matrix_rank(mergedMatrix)

    print("macierz A rozszerzona o macierz B: \n", mergedMatrix)
    # stosujemy tw. Kronckera - Capellego i sprawdzamy czy uklady spelniaja jego warunki
    if rankA != rankM: # jesli rzedy macierzy sa rozne to uklad jest sprzeczny
        return "Uklad sprzeczny !"
    elif rankA == rankM and rankM < n: # jesli rzedy macierzy sa sobie rowne ale mniejsze niz ilosc niewiadomych to uklad jest nieoznaczony
        return "Uklad nieoznaczony !"
    else: # w przeciwnym przypadku uklad jest oznaczony
        for k in range(n):
            partial_swapping(matrixA, matrixB, k, n) # wykonujemy tutaj zamiane wierszy w celu unikniecia bledu wynikajacego
            #z zaokraglenia przez typ danych
            tmp = matrixA[k][k]

            for j in range(k, n):
                matrixA[k][j] /= tmp

            matrixB[k] /= tmp

            for i in range(n):
                if i != k and matrixA[i][k] != 0:
                    factor = matrixA[i][k]

                    for j in range(k, n):
                        matrixA[i][j] -= factor * matrixA[k][j]

                    matrixB[i] -= factor * matrixB[k]

        print("macierz A po wykonaniu metody elminacji: \n", matrixA)
        return "rozwiazanie(od x1 do xn): ", str(matrixB)


def partial_swapping(A, B, k, n):
    for i in range(k + 1, n):
        if np.fabs(A[i][k]) > np.fabs(A[k][k]):
            for j in range(k, n):
                A[k][j], A[i][j] = A[i][j], A[k][j]

            B[k], B[i] = B[i], B[k]



# for i in range(n):
        #     for j in range(n):
        #         if mergedMatrix[i][i] == 0.0:
        #             for k in range(n):
        #                 j += 1
        #         if i != j:
        #             tmp = float(mergedMatrix[j][i] / mergedMatrix[i][i])
        #             for k in range(n + 1):
        #                 mergedMatrix[j][k] = float(mergedMatrix[j][k] - tmp * mergedMatrix[i][k])
        #
        # return prepare_result(mergedMatrix, solutionMatrix, n)

# def prepare_result(matrix, result, n):
#     for i in range(n):
#         result[i] = float((matrix[i][n]) / matrix[i][i])
#
#     return result

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
