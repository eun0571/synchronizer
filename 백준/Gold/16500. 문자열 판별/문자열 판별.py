import sys

a = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
words = []
for i in range(n):
    words.append(sys.stdin.readline().strip())
dp = [0 for _ in range(len(a) + 1)]
dp[0] = 1
for i in range(1, len(a) + 1):
    for word in words:
        if dp[i - len(word)] and a[i - len(word) : i] == word:
            dp[i] = 1
print(dp[-1])
