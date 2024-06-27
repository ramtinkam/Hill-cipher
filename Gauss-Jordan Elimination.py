def determinant(A):
    n = len(A[0])
    mulTot = 1
    det = 1
    for i in range(n):
        nonZeroRow = n
        for j in range(i, n):
            if (A[j][i] != 0):
                nonZeroRow = j
                break
        if nonZeroRow != i:
            for j in range(0, n):
                A[nonZeroRow][j], A[i][j] = A[i][j], A[nonZeroRow][j]
            # if ((nonZeroRow - i) % 2 == 1):
            #     det *= -1
            det = det * -1 * ((nonZeroRow - i) & 1)
        for j in range(i + 1, n):
            x = A[i][i]
            y = A[j][i]
            for k in range(n):
                A[j][k] = (x * A[j][k]) - (y * A[i][k])
            mulTot *= x

    for i in range(n):
        det *= A[i][i]
    return det/mulTot


A = [[2, 4, -2], [1, 2, 4], [-3, -3, 8]]
print(determinant(A))
print(A)
