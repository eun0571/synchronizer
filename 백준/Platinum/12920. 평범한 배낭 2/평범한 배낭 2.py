import sys

n, m = map(int, sys.stdin.readline().split())
dp = [0] * (m + 1)

for i in range(n):
    w, v, k = map(int, sys.stdin.readline().split())
    a = 1
    while k > 0:
        count = min(a, k)
        k -= count
        for i in range(m, w * count - 1, -1):
            dp[i] = max(dp[i - w * count] + v * count, dp[i])
        a *= 2
print(dp[-1])
