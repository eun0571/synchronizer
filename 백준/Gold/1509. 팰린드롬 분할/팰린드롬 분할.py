import sys

l = list(sys.stdin.readline().strip())
n = len(l)
dp = [[0 if i != j else 1 for i in range(n)] for j in range(n)]

for i in range(1, n):
    if l[i - 1] == l[i]:
        dp[i - 1][i] = 1
for length in range(3, n + 1):
    for i in range(length - 1, n):
        j = i - length + 1
        if l[i] == l[j] and dp[j + 1][i - 1]:
            dp[j][i] = 1

min_cut = [sys.maxsize for _ in range(n)]
min_cut[0] = 0
for i in range(n):
    if dp[0][i]:
        min_cut[i] = 0
    else:
        for j in range(i):
            if dp[j + 1][i]:
                min_cut[i] = min(min_cut[i], min_cut[j] + 1)

print(min_cut[-1] + 1)
