import sys

input = sys.stdin.readline
n = int(input())

dp = [1 for _ in range(n + 1)]
dp[0] = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    for j in range(a + 1, b + 1):
        dp[j] = 0
print(dp.count(1))
