import sys

input = sys.stdin.readline
n = int(input())
l = [tuple(map(int, input().split())) for _ in range(n)]
l.sort(key=lambda x: x[1], reverse=True)
last = sys.maxsize
for i in range(n):
    if l[i][1] <= last:
        last = l[i][1] - l[i][0]
    else:
        last = last - l[i][0]
print(last)
