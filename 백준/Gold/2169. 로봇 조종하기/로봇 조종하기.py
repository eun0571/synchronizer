import sys

n, m = map(int, sys.stdin.readline().split())
value = []
for i in range(n):
    value.append(list(map(int, sys.stdin.readline().split())))

dp = [[-sys.maxsize for j in range(m)] for i in range(n)]

for i in range(n):
    tmp = [-sys.maxsize for j in range(m)]
    if i == 0:
        for j in range(m):
            if j == 0:
                dp[i][j] = value[i][j]
            else:
                dp[i][j] = value[i][j] + dp[i][j - 1]
    else:
        for j in range(m):
            if j == 0:
                dp[i][j] = value[i][j] + dp[i - 1][j]
            else:
                dp[i][j] = value[i][j] + max(dp[i - 1][j], dp[i][j - 1])
    if i != 0:
        for j in range(m - 1, -1, -1):
            if j == m - 1:
                tmp[j] = value[i][j] + dp[i - 1][j]
            else:
                tmp[j] = value[i][j] + max(dp[i - 1][j], tmp[j + 1])
    for j in range(m):
        dp[i][j] = max(dp[i][j], tmp[j])

print(dp[-1][-1])
