import sys
from collections import deque

n = int(sys.stdin.readline())

a = deque()

for i in range(n):
    ps = sys.stdin.readline().strip()
    for j in range(len(ps)):
        if ps[j] == "(":
            a.append(1)
        else:
            try:
                a.pop()
            except:
                print("NO")
                break
    else:
        if len(a) == 0:
            print("YES")
        else:
            print("NO")
    a.clear()
