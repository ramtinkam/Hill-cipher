def minor(A, i, j):
    temp = A[:i] + A[i+1:]
    return [row[:j] + row[j + 1:] for row in temp]


def determinant(A):
    if (len(A) == 2):
        return A[0][0] * A[1][1] - A[1][0] * A[0][1]
    det = 0
    for i in range(len(A)):
        det += ((-1) ** i) * A[0][i] * determinant(minor(A, 0, i))
    return det


A = [[2, 4, -2], [1, 2, 4], [-3, -3, 8]]
print(determinant(A))
