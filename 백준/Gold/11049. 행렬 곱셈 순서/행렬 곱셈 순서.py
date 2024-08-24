import sys

n = int(sys.stdin.readline())
p = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    p.append(a)
    if i == n - 1:
        p.append(b)

m = [[sys.maxsize for j in range(n)] for i in range(n)]


def MCM(p, n):
    for chain in range(n + 1):
        for i in range(n - chain):
            j = i + chain
            if i == j:
                m[i][j] = 0
            else:
                for k in range(i, j):
                    new = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                    if new < m[i][j]:
                        m[i][j] = new


MCM(p, n)
print(m[0][n - 1])
