import sys

a = sys.stdin.readline().strip()
a = " " + a
b = sys.stdin.readline().strip()
b = " " + b
n = len(a)
m = len(b)
dp2 = [[0 for i in range(m)] for j in range(n)]
dp = [[0 for i in range(m)] for j in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            dp2[i][j] = 3
        elif dp[i - 1][j] >= dp[i][j - 1]:
            dp[i][j] = dp[i - 1][j]
            dp2[i][j] = 2
        else:
            dp[i][j] = dp[i][j - 1]
            dp2[i][j] = 1

li = [m]
for i in range(n - 1, 0, -1):
    for j in range(m - 1, 0, -1):
        if j < li[-1]:
            if dp2[i][j] == 3:
                li.append(j)
                break
            elif dp2[i][j] == 2:
                break
li.sort()

result = ""
for i in li[:-1]:
    result += b[i]

print(dp[-1][-1])
if result:
    print(result)
