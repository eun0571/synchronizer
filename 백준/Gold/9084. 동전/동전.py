import sys
n = int(sys.stdin.readline())

for i in range(n):
    m = int(sys.stdin.readline())
    coins = sorted(list(map(int, sys.stdin.readline().split())))
    target = int(sys.stdin.readline())
    dp = [0 for i in range(target + 1)]
    dp[0] = 1
    for coin in coins:
        for i in range(1, target + 1):
            if i - coin >= 0:
                dp[i] += dp[i - coin]
    print(dp[-1])
