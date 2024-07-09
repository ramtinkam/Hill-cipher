def minor(A, i, j):
    temp = A[:i] + A[i + 1:]
    return [row[:j] + row[j + 1:] for row in temp]


def determinant(A, memo):
    n = len(A)
    if n == 2:
        return A[0][0] * A[1][1] - A[1][0] * A[0][1]

    # Use a tuple of tuples as the key for memoization to make it hashable
    key = tuple(tuple(row) for row in A)
    if key in memo:
        return memo[key]

    det = 0
    for i in range(n):
        minor_matrix = minor(A, 0, i)
        det += ((-1) ** i) * A[0][i] * determinant(minor_matrix, memo)

    memo[key] = det
    return det


A = []
n = int(input())
for _ in range(n):
    r = list(map(float, input().split()))
    A.append(r)

memo = {}
number = int(determinant(A, memo))
print(number)
