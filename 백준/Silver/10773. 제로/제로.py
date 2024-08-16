import sys
from collections import deque

n = int(sys.stdin.readline())

a = []

for i in range(n):
    num = int(sys.stdin.readline())
    if num:
        a.append(num)
    else:
        a.pop()

print(sum(a))
