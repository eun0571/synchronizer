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
        for k in range(1, num+1):
            if i - k * coin >= 0:
                dp[i] += dp[i - k * coin]
            else:
                break
print(dp[t])
