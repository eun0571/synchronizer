import sys
from collections import deque

n, m, h = map(int, sys.stdin.readline().split())

tomato = [
    [list(map(int, sys.stdin.readline().split())) for _ in range(m)] for _ in range(h)
]

dx = [1, 0, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1, 0]
dz = [0, 0, 1, 0, 0, -1]

q = deque()

for z in range(h):
    for y in range(m):
        for x in range(n):
            if tomato[z][y][x] == 1:
                q.append((x, y, z, 1))


def tomatomato():
    while q:
        cx, cy, cz, cd = q.popleft()
        for d in range(6):
            nx = cx + dx[d]
            ny = cy + dy[d]
            nz = cz + dz[d]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if not tomato[nz][ny][nx] or tomato[nz][ny][nx] > cd + 1:
                    tomato[nz][ny][nx] = cd + 1
                    q.append((nx, ny, nz, cd + 1))


tomatomato()

max_day = 0
for z in range(h):
    for y in range(m):
        for x in range(n):
            if not tomato[z][y][x]:
                print(-1)
                sys.exit(0)
            max_day = max(max_day, tomato[z][y][x])
print(max_day - 1)
