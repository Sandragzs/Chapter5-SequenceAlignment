#49
def lcs3(a, b, c):
    n, m, l = len(a), len(b), len(c)
    dp = [[[0]*(l+1) for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(1, l+1):
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1 if a[i-1]==b[j-1]==c[k-1] else \
                              max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

    i, j, k = n, m, l
    A, B, C = [], [], []
    while i or j or k:
        if i and j and k and a[i-1]==b[j-1]==c[k-1]:
            A.append(a[i-1]); B.append(b[j-1]); C.append(c[k-1])
            i, j, k = i-1, j-1, k-1
        elif i and dp[i][j][k]==dp[i-1][j][k]:
            A.append(a[i-1]); B.append('-'); C.append('-'); i-=1
        elif j and dp[i][j][k]==dp[i][j-1][k]:
            A.append('-'); B.append(b[j-1]); C.append('-'); j-=1
        else:
            A.append('-'); B.append('-'); C.append(c[k-1]); k-=1

    return dp[n][m][l], ''.join(A[::-1]), ''.join(B[::-1]), ''.join(C[::-1])


a, b, c = "ATTCTACCAGTCCCCATTACTAGAGCCGC", "GTCACGTATGCGACGTTCCTCCTTCAT", "GCCACGCTCGACGCCCTTGCTCGAC"
s, x, y, z = lcs3(a, b, c)
print(s, x, y, z, sep='\n')