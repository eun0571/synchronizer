import sys

n = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for _ in range(n)]
if n <= 2:
    print(sum(l))
else:
    dp = [0 for i in range(n + 1)]
    dp[0] = 0
    dp[1] = l[0]
    dp[2] = l[0] + l[1]
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 3] + l[i - 2] + l[i - 1], dp[i - 2] + l[i - 1])
    
    print(dp[n])
