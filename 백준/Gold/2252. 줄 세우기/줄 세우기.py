import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

g = [[] for i in range(n)]

in_dgr = [0 for _ in range(n)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    g[x - 1].append(y - 1)
    in_dgr[y - 1] += 1

q = deque()
answer = []


def topological_sort():
    for i in range(n):
        if in_dgr[i] == 0:
            q.append(i)

    while q:
        a = q.popleft()
        answer.append(a)
        for i in g[a]:
            in_dgr[i] -= 1
            if in_dgr[i] == 0:
                q.append(i)


topological_sort()


for i in answer:
    print(i + 1, end=" ")
