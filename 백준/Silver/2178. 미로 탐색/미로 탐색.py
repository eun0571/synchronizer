import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

matrix = [[] for j in range(n)]

for i in range(n):
    for j in sys.stdin.readline().strip():
        matrix[i].append(int(j))

q = deque()

navi = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def maze(x, y):
    q.append((x, y, 1))
    matrix[x][y] = 0
    candy = []
    while q:
        a = q.popleft()
        
        x = a[0]
        y = a[1]
        for i in range(4):
            X = x + navi[i][0]
            Y = y + navi[i][1]

            if -1 < X < n and -1 < Y < m and matrix[X][Y]:
                matrix[X][Y] = 0
                if (X, Y) == (n - 1, m - 1):
                    return a[2]+1
                q.append((X, Y, a[2] + 1))
    return min(candy)


print(maze(0, 0))
