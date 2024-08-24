import sys

l = list(sys.stdin.readline().strip())
n = len(l)

dp = [[0 if i != j else 1 for i in range(n + 1)] for j in range(n + 1)]

for i in range(1, n):
    if l[i - 1] == l[i]:
        dp[i][i + 1] = 1
# 길이 3이상
for length in range(3, n + 1):
    for i in range(n - length + 2):
        j = i + length - 1
        if l[i - 1] == l[j - 1]:
            if dp[i + 1][j - 1] or (dp[i + 1][j] and dp[i][j - 1]):
                dp[i][j] = 1

min_cuts = [float("inf")] * n

for i in range(1, n + 1):
    if dp[1][i]:  # 처음부터 i까지가 팰린드롬인 경우
        min_cuts[i - 1] = 0
    else:
        for j in range(1, i):
            if dp[j + 1][i]:
                min_cuts[i - 1] = min(min_cuts[i - 1], min_cuts[j - 1] + 1)

# 결과 출력
print(min_cuts[-1] + 1)
