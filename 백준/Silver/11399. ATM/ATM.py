import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
l.sort()
result = 0
for i in range(n):
    result += (n - i) * l[i]
print(result)
