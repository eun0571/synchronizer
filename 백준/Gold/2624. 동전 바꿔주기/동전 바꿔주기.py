import sys

t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
coins = []


for i in range(n):
    a, b = tuple(map(int, sys.stdin.readline().split()))
    coins.append((a, b))


dp = [0 for _ in range(t + 1)]
dp[0] = 1
for coin, num in coins:
    for i in range(t, 0, -1):
        for k in range(num, 0, -1):
            if i - k * coin >= 0 and dp[i - k * coin]:
                dp[i] += dp[i - k * coin]
print(dp[t])
