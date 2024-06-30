def minor(A, i, j):
    temp = A[:i] + A[i+1:]
    return [row[:j] + row[j + 1:] for row in temp]


def determinant(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0] * A[1][1] - A[1][0] * A[0][1]
    tempA = [[determinant(minor(A, 0, 0)), determinant(minor(A, 0, n - 1))],
             [determinant(minor(A, n - 1, 0)), determinant(minor(A, n - 1, n - 1))]]
    det = tempA[0][0] * tempA[1][1] - tempA[1][0] * tempA[0][1]
    divideVal = determinant(minor(minor(A, 0, 0), n - 2, n - 2))
    return det / divideVal


# Testing determinant of matrices used in the article

A = [[10, 1, 3, -7], [5, 4, 1, 12], [0, 2, 10, 1], [4, 3, 20, 11]]
print(determinant(A))

A = [[5, 9, 7], [8, 12, 13], [-1, 15, 4]]
print(determinant(A))
