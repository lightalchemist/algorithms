
def print_matrix(A):
    m = len(A)
    n = len(A[0])
    for i in range(m):
        # for j in range(n):
        print " ".join(map(str, A[i]))

import numpy as np
def lcs(X, Y):
    """Computes the least common subsequence of string X and Y."""
    m, n = len(X), len(Y)
    A = [[0] * (n+1) for _ in range(m+1)]

    A = np.zeros((m+1, n+1), dtype=np.uint)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                A[i][j] = 1 + A[i-1][j-1]
            else:
                A[i][j] = max(A[i-1][j], A[i][j-1])

    # print_matrix(A)
    print(A)
    return A[m][n]


def test():
    X = "XMJYAUZ"
    Y = "MZJAWXU"
    # assert lcs(X, Y) == 4
    print(lcs(X, Y))


if __name__ == "__main__":
    test()
