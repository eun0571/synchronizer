import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

matrix = [[0 for i in range(n)] for j in range(n)]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x - 1][y - 1] = 1
    matrix[y - 1][x - 1] = 1
# DFS 재귀로 구현하기
visited = [0 for i in range(n)]


def DFS(v):
    print(v + 1, end=" ")
    for i in range(n):
        if matrix[v][i] and not visited[i]:
            visited[i] = 1
            DFS(i)


visited[v - 1] = 1
# DFS(v - 1)
# DFS 스택으로 구현하기
visited = [0 for i in range(n)]
stack = deque()


def DFS_stack(v):
    stack.append(v)
    while stack:
        a = stack.pop()
        if visited[a] == 0:
            visited[a] = 1
            print(a + 1, end=" ")
            # 작은 번호의 정점을 먼저 처리하기 위해 정순으로 스택에 넣음
            for i in range(n - 1, -1, -1):
                if matrix[a][i] and not visited[i]:
                    stack.append(i)


DFS_stack(v - 1)
print()  # 줄바꿈
##########################################################
# BFS 구현하기

visited = [0 for i in range(n)]
q = deque()


def BFS(v):
    q.append(v)
    visited[v] = 1
    while q:
        a = q.popleft()
        print(a + 1, end=" ")
        for i in range(n):
            if matrix[a][i] and not visited[i]:
                visited[i] = 1
                q.append(i)


visited[v - 1] = 1
BFS(v - 1)
