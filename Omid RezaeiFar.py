def minor(A, i, j):
    temp = A[:i] + A[i + 1:]
    return [row[:j] + row[j + 1:] for row in temp]


def determinant(A):
    global flag
    if flag:
        return 0
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    tempA = [[determinant(minor(A, 0, 0)), determinant(minor(A, 0, n - 1))],
             [determinant(minor(A, n - 1, 0)), determinant(minor(A, n - 1, n - 1))]]
    det = tempA[0][0] * tempA[1][1] - tempA[0][1] * tempA[1][0]
    divideVal = determinant(minor(minor(A, 0, 0), n - 2, n - 2))
    if (divideVal == 0):
        return 0
    return det / divideVal


# def change_matrix(A):
#     n = len(A)
#     for i in range(n):
#         for j in range(i + 1, n):
#             # Swap rows
#             A[i], A[j] = A[j], A[i]
#             if not is_singular(minor(minor(A, 0, 0), n - 2, n - 2)):
#                 return A
#             # Swap back if the minor is still singular
#             A[i], A[j] = A[j], A[i]
#             # Swap columns
#             for k in range(n):
#                 A[k][i], A[k][j] = A[k][j], A[k][i]
#             if not is_singular(minor(minor(A, 0, 0), n - 2, n - 2)):
#                 return A
#             # Swap back if the minor is still singular
#             for k in range(n):
#                 A[k][i], A[k][j] = A[k][j], A[k][i]
#     return A


# def is_singular(M):
#     return determinant(M) == 0


# Read input matrix
A = []
n = int(input())
for _ in range(n):
    r = list(map(float, input().split()))
    A.append(r)

flag = 0
number = int(determinant(A))
print(number)
