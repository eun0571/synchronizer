import sys
from collections import deque

n = int(sys.stdin.readline())

a = deque([n - i for i in range(n)])

while len(a) > 1:
    a.pop()
    a.appendleft(a.pop())

print(a[0])
