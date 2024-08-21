import sys
from collections import deque

n = int(sys.stdin.readline())

maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

visited = [[-1 for _ in range(n)] for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(q, visited, maze, n):
    while q:
        c_x, c_y, broken_wall = q.popleft()

        if c_x == n - 1 and c_y == n - 1:
            return broken_wall

        for i in range(4):
            n_x = c_x + dx[i]
            n_y = c_y + dy[i]
            if 0 <= n_x < n and 0 <= n_y < n:
                wall = maze[n_x][n_y] == 0
                if visited[n_x][n_y] == -1 or visited[n_x][n_y] > broken_wall + wall:
                    visited[n_x][n_y] = broken_wall + wall
                    if wall:
                        q.append((n_x, n_y, broken_wall + 1))
                    else:
                        q.appendleft((n_x, n_y, broken_wall))


q = deque([(0, 0, 0)])
visited[0][0] = 0

print(bfs(q, visited, maze, n))
