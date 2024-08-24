import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))


dp = [[0 if i != j else 1 for i in range(n + 1)] for j in range(n + 1)]

for i in range(n - 1, 0, -1):
    for j in range(n, i, -1):
        if l[i - 1] == l[j - 1]:
            if dp[i + 1][j - 1] or (dp[i + 1][j] and dp[i][j - 1]):
                dp[i][j] = 1

m = int(sys.stdin.readline())
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    print(dp[x][y])
