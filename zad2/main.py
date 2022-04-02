from matrixOperations import matrix_A, matrix_B
from gauss_jordan import matrix_to_gauss_jordan
from reader import read_from_csv

if __name__ == '__main__':
    try:
        content, n = read_from_csv()
        print(content)
        matrixA = matrix_A(content, n)
        matrixB = matrix_B(content, n)
        print(matrixA)
        print(matrixB)
        jordan = matrix_to_gauss_jordan(matrixA, matrixB, n)
        print(jordan)
    except:
        print("Nie udalo sie wczytac pliku")
