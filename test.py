# GPT
def matrix_multiply(A, B):
    # Validate that both matrices are non-empty
    if not A or not B:
        raise ValueError("Matrices must not be empty")

    # Validate that each matrix is rectangular
    if not all(isinstance(row, list) for row in A + B):
        raise ValueError("Matrices must contain lists as rows")

    if not all(len(row) == len(A[0]) for row in A):
        raise ValueError("A must be rectangular")

    if not all(len(row) == len(B[0]) for row in B):
        raise ValueError("B must be rectangular")

    # Inner dimensions must match
    if len(A[0]) != len(B):
        raise ValueError("Incompatible matrix dimensions")

    result = []

    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(A[0])):
                total += A[i][k] * B[k][j]
            row.append(total)

        result.append(row)

    return result


A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print(matrix_multiply(A, B))
# [[19, 22], [43, 50]]
