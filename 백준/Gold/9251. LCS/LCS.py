import sys

a = sys.stdin.readline().strip()
a = " " + a
b = sys.stdin.readline().strip()
b = " " + b
n = len(a)
m = len(b)

dp = [[0 for i in range(m)] for j in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
print(dp[-1][-1])
