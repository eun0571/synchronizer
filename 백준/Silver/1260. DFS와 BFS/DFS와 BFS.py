import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

matrix = [[0 for i in range(n)] for j in range(n)]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x - 1][y - 1] = 1
    matrix[y - 1][x - 1] = 1
##########################################################
visited = [0 for i in range(n)]


def DFS(v):
    print(v + 1, end=" ")
    for i in range(n):
        if matrix[v][i] and not visited[i]:
            visited[i] = 1
            DFS(i)


visited[v - 1] = 1
DFS(v - 1)
##########################################################
print()
##########################################################
visited = [0 for i in range(n)]
q = deque()


def BFS(v):
    q.append(v)
    visited[v] = 1
    while len(q):
        a = q.popleft()
        print(a + 1, end=" ")
        for i in range(n):
            if matrix[a][i] and not visited[i]:
                visited[i] = 1
                q.append(i)


visited[v - 1] = 1
BFS(v - 1)
