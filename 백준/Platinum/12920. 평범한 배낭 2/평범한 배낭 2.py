import sys

n, m = map(int, sys.stdin.readline().split())
dp = [0] * (m + 1)

for _ in range(n):
    weight, value, count = map(int, sys.stdin.readline().split())
    i = 1
    while count > 0:
        actual_count = min(i, count)
        count -= actual_count
        for j in range(m, actual_count * weight - 1, -1):
            dp[j] = max(dp[j], dp[j - actual_count * weight] + actual_count * value)
        i *= 2

print(max(dp))
