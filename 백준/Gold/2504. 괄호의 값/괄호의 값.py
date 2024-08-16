import sys
from collections import deque


ps = sys.stdin.readline().strip()
a = deque()

try:
    for j in range(len(ps)):
        if ps[j] == "(":
            a.append("(")
        elif ps[j] == ")":
            tmp = 0
            while True:
                top = a.pop()
                if top == "(":
                    a.append(2 * tmp if tmp else 2)
                    break
                elif isinstance(top, int):
                    tmp += top
                else:
                    raise 0
        elif ps[j] == "[":
            a.append("[")
        elif ps[j] == "]":
            tmp = 0
            while True:
                top = a.pop()
                if top == "[":
                    a.append(3 * tmp if tmp else 3)
                    break
                elif isinstance(top, int):
                    tmp += top
                else:
                    raise 0
    print(sum(a))
except:
    print(0)
