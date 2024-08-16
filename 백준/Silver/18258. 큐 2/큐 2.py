import sys
from collections import deque

n = int(sys.stdin.readline())

a = deque()

for i in range(n):
    c = list(sys.stdin.readline().split())

    if c[0] == "push":
        a.append(c[1])
    elif c[0] == "pop":
        print(a.popleft()) if len(a) else print(-1)
    elif c[0] == "size":
        print(len(a))
    elif c[0] == "empty":
        print(int(len(a) == 0))
    elif c[0] == "front":
        print(a[0]) if len(a) else print(-1)
    elif c[0] == "back":
        print(a[-1]) if len(a) else print(-1)
