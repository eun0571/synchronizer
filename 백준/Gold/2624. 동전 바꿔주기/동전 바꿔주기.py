import sys

input = sys.stdin.readline
t = int(input())
n = int(input())
coins = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(t + 1)]
dp[0] = 1
for coin, num in coins:
    for i in range(t, -1, -1):
        for j in range(1, num + 1):
            if i + j * coin <= t and dp[i]:
                dp[i + j * coin] += dp[i]
            else:
                break
print(dp[-1])
