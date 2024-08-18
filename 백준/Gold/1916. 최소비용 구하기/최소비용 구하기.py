import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

e = [[] for _ in range(n)]

for _ in range(m):
    x, y, c = map(int, sys.stdin.readline().split())
    e[x - 1].append((y - 1, c))

start, end = map(int, sys.stdin.readline().split())

q = deque()

cost = [sys.maxsize for _ in range(n)]
cost[start - 1] = 0


def BFS(start):
    q.append(start)
    while q:
        a = q.popleft()
        for i in e[a]:
            if cost[a] + i[1] < cost[i[0]]:
                cost[i[0]] = cost[a] + i[1]
                if i[0] not in q:
                    q.append(i[0])


BFS(start - 1)

print(cost[end - 1])
