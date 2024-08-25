import sys

n, k = map(int, sys.stdin.readline().split())
goods = []
for _ in range(n):
    goods.append(list(map(int, sys.stdin.readline().split())))

dp = [-1]*(k + 1)
dp[0] = 0
for w, v in goods:
    for i in range(k, w-1, -1):
        if dp[i - w] != -1:
            dp[i] = max(dp[i], dp[i - w] + v)

print(max(dp))
