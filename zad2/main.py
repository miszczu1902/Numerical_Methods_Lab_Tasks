from matrix_operations import matrix_a, matrix_b
from gauss_jordan import matrix_to_gauss_jordan
from reader import read_from_csv


if __name__ == '__main__':
    content, n = read_from_csv()
    matrixA = matrix_a(content, n)
    matrixB = matrix_b(content, n)
    jordan = matrix_to_gauss_jordan(matrixA, matrixB, n)
    print(jordan)
