def coefficient(n, m):
    C = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(n+1):
        C[i][0] = 1
    for j in range(1, m+1):
        C[j][j] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            C[i][j] = C[i-1][j] + C[i-1][j-1]
    return C[n][m]
print(coefficient(6, 2))
