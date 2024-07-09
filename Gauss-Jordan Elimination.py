def determinant(A, n):
    mulTot = 1
    det = 1
    for i in range(n):
        nonZeroRow = n
        for j in range(i, n):
            if (A[j][i] != 0):
                nonZeroRow = j
                break
        if (nonZeroRow == n):
            return 0
        if nonZeroRow != i:
            for j in range(0, n):
                A[nonZeroRow][j], A[i][j] = A[i][j], A[nonZeroRow][j]
            if ((nonZeroRow - i) & 1):
                det *= -1
        for j in range(i + 1, n):
            x = A[i][i]
            y = A[j][i]
            for k in range(n):
                A[j][k] = (x * A[j][k]) - (y * A[i][k])
            mulTot *= x

    for i in range(n):
        det *= A[i][i]
    return det/mulTot


A = []
n = int(input())
for _ in range(n):
    r = list(map(float, input().split()))
    A.append(r)
number = int(determinant(A, n))
print(number)
