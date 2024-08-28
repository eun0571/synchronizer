import sys

n = int(sys.stdin.readline())
dp = [sys.maxsize for _ in range(n + 1)]
dp[1] = 0
for i in range(1, n + 1):
    if i + 1 <= n:
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)
    if i * 2 <= n:
        dp[i * 2] = min(dp[i * 2], dp[i] + 1)
    if i * 3 <= n:
        dp[i * 3] = min(dp[i * 3], dp[i] + 1)

c = dp[n]
print(c)
while c >= 0:
    print(n, end=" ")
    if n % 3 == 0 and dp[n // 3] == c - 1:
        n //= 3
    elif n % 2 == 0 and dp[n // 2] == c - 1:
        n //= 2
    elif dp[n - 1] == c - 1:
        n -= 1
    c -= 1
