import sys

n = int(sys.stdin.readline())
weights = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
beads = list(map(int, sys.stdin.readline().split()))
heaviest = sum(weights)
dp = [0 for i in range(heaviest + 1)]
dp[0] = 1

for weight in weights:
    dp2 = [0 for i in range(heaviest + 1)]
    for i in range(heaviest, -1, -1):
        if dp[i]:
            if i + weight <= heaviest:
                dp2[i + weight] = 1
            if abs(i - weight) <= heaviest:
                dp2[abs(i - weight)] = 1
    for i in range(heaviest, 0, -1):
        if dp2[i]:
            dp[i] = 1

for i in beads:
    if i <= heaviest and dp[i]:
        print("Y", end=" ")
    else:
        print("N", end=" ")
