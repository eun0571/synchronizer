import sys
from collections import deque

n = int(sys.stdin.readline())

a = deque()


for i in range(n):
    command = list(sys.stdin.readline().split())
    if command[0] == "push":
        a.append(command[1])
    elif command[0] == "pop":
        if len(a) > 0:
            print(a.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(a))
    elif command[0] == "empty":
        print(int(len(a) == 0))
    elif command[0] == "top":
        if len(a) == 0:
            print(-1)
        else:
            print(a[-1])
