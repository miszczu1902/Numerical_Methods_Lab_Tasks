import numpy as np


def matrix_to_gauss_jordan(matrixA, matrixB, n):
    # przygotowanie macierzy
    matrixBTmp = np.array(matrixB).reshape(n, 1)
    mergedMatrix = np.concatenate((matrixA, matrixBTmp), axis=1)

    # liczymy rzad dla: pierwotnej i nowej macierzy (macierz A rozszerzona o macierz B)
    rankA = np.linalg.matrix_rank(matrixA)
    rankM = np.linalg.matrix_rank(mergedMatrix)

    print("macierz A rozszerzona o macierz B: \n", mergedMatrix)
    # stosujemy tw. Kroneckera - Capellego i sprawdzamy czy uklady spelniaja jego warunki
    if rankA != rankM: # jesli rzedy macierzy sa rozne to uklad jest sprzeczny
        return "Uklad sprzeczny !"
    elif rankA == rankM and rankA < n: # jesli rzedy macierzy sa sobie rowne ale mniejsze niz ilosc niewiadomych to uklad jest nieoznaczony
        return "Uklad nieoznaczony !"
    else: # w przeciwnym przypadku uklad jest oznaczony
        for k in range(n):
            partial_swapping(matrixA, matrixB, k, n) # wykonujemy tutaj zamiane elementow w celu unikniecia bledu wynikajacego
            #z zaokraglenia przez typ danych
            tmp = matrixA[k][k]

            for j in range(k, n):
                matrixA[k][j] /= tmp

            matrixB[k] /= tmp

            for i in range(n): # redukujemy wiersz do wiersza z zerami i jedynka
                if i != k and matrixA[i][k] != 0:
                    factor = matrixA[i][k] # gdy element nie jest na glownej przekatnej macierzy
                    # to ustawiamy wartosc pomocniczego wspolczynnika

                    for j in range(k, n):
                        matrixA[i][j] -= factor * matrixA[k][j] # redukujemy element z wiersza do 0

                    matrixB[i] -= factor * matrixB[k] # redukujemy element z macierzy B o wartosc jak wczesniej
                    # to bedzie nasz wynik

        print("macierz A po wykonaniu metody elminacji: \n", matrixA)
        return "rozwiazanie(od x1 do xn): ", str(matrixB)


def partial_swapping(A, B, k, n):
    for i in range(k + 1, n):
        if np.fabs(A[i][k]) > np.fabs(A[k][k]):
            for j in range(k, n):
                A[k][j], A[i][j] = A[i][j], A[k][j]

            B[k], B[i] = B[i], B[k]