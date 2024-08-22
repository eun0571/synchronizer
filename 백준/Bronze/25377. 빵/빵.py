import sys

n = int(sys.stdin.readline())

result = []
for i in range(n):
    time, left = map(int, sys.stdin.readline().split())
    if left - time > 0:
        result.append(left)
if result:
    result.sort()
    print(result[0])
else:
    print(-1)
