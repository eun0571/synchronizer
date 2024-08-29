import sys

input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
k = int(input())
m = l[-1] * k
dp = [0 for _ in range(m + 1)]
dp[0] = 1
tmp = [0 for _ in range(m + 1)]
for num_coin in range(1, k + 1):
    for j in range(m + 1):
        if dp[j]:
            for coin in l:
                if j + coin <= m:
                    tmp[j + coin] = 1
                else:
                    break
    for j in range(m + 1):
        dp[j] = dp[j] | tmp[j]

if dp.count(0):
    point = dp.index(0)
    if point % 2 == 0:
        print(f"holsoon win at {point}")
    else:
        print(f"jjaksoon win at {point}")
else:
    if m % 2 == 0:
        print(f"jjaksoon win at {m+1}")

    else:
        print(f"holsoon win at {m+1}")
