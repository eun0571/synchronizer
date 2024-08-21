import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

e = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    e[a - 1].append(b - 1)
    e[b - 1].append(a - 1)

for i in range(n):
    e[i].sort()

visited = [0 for _ in range(n)]


def dfs(e, v):
    print(v + 1, end=" ")
    for i in e[v]:
        if not visited[i]:
            visited[i] = 1
            dfs(e, i)


visited[v - 1] = 1
dfs(e, v - 1)
print()


def bfs():
    while q:
        a = q.popleft()
        print(a + 1, end=" ")
        for i in e[a]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)


visited = [0 for _ in range(n)]
visited[v - 1] = 1
q = deque([v - 1])
bfs()
