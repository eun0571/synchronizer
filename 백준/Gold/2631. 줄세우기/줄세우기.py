import sys

input = sys.stdin.readline
n = int(input())
l = [0] + [int(input()) for _ in range(n)]
# lis 문제다
dp = [0 for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(i):
        if l[i] > l[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
