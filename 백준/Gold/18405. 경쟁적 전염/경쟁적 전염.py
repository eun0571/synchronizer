import sys
from heapq import heappush, heappop

n, k = map(int, sys.stdin.readline().split())
plate = [list(map(int, sys.stdin.readline().split())) for i in range(n)]


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

s, x, y = map(int, sys.stdin.readline().split())

heap = []
for i in range(n):
    for j in range(n):
        if plate[i][j]:
            heappush(heap, (0, plate[i][j], i, j))

while heap:
    time, v, cx, cy = heappop(heap)
    if time <= s and cx == x - 1 and cy == y - 1:
        print(v)
        sys.exit(0)
    elif time > s:
        print(0)
        sys.exit(0)

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not plate[nx][ny]:
            plate[nx][ny] = v
            heappush(heap, (time + 1, v, nx, ny))
