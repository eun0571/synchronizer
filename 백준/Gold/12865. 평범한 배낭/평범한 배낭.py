import sys

n, k = map(int, sys.stdin.readline().split())
w = [0]
v = [0]
for _ in range(n):
    weight, value = map(int, sys.stdin.readline().split())
    w.append(weight)
    v.append(value)
dp = [[None if j else 0 for j in range(k + 1)] for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j - w[i] >= 0:
            if dp[i - 1][j - w[i]] != None and dp[i - 1][j] != None:
                dp[i][j] = max(dp[i - 1][j - w[i]] + v[i], dp[i - 1][j])
            elif dp[i - 1][j - w[i]] != None:
                dp[i][j] = dp[i - 1][j - w[i]] + v[i]
            elif dp[i - 1][j] != None:
                dp[i][j] = dp[i - 1][j]
        elif dp[i - 1][j] != None:
            dp[i][j] = dp[i - 1][j]

result = 0
for i in range(1,k+1):
    if dp[-1][i]:
        result = max(result,dp[-1][i])
print(result)