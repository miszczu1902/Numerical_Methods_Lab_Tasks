from matrixOperations import generate_unit_matrix, matrix_A, matrix_B
from gauss_jordan import matrix_to_gauss_jordan


if __name__ == '__main__':
    n = 3
    matrixA = matrix_A(n)
    matrixB = matrix_B(n)
    jordan, result = matrix_to_gauss_jordan(matrixA, matrixB, n)
    print(jordan)
    print("============================================================================")
    print(result)



