import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

map = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]

start = ()
dest = ()

q = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
water = []

for i in range(n):
    for j in range(m):
        if map[i][j] == "*":
            water.append((i, j, "*", 0))
        elif map[i][j] == "S":
            start = (i, j, "S", 0)
        elif map[i][j] == "D":
            dest = (i, j)

q.append(start)
for i in range(len(water)):
    q.append(water[i])

while q:
    cx, cy, id, distance = q.popleft()
    if cx == dest[0] and cy == dest[1]:
        print(distance)
        sys.exit(0)
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if id == "*":
                if map[nx][ny] == "." or map[nx][ny] == "S":
                    map[nx][ny] = "*"
                    q.append((nx, ny, "*", distance + 1))
            elif id == "S" and map[cx][cy] != "*":
                if map[nx][ny] == "." or map[nx][ny] == "D":
                    map[nx][ny] = "S"
                    map[cx][cy] = "."
                    q.append((nx, ny, "S", distance + 1))
print("KAKTUS")
