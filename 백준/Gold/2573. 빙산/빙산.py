from collections import deque

# 방향벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS를 사용하여 빙산 덩어리를 카운트하는 함수
def bfs(x, y, visited, iceberg):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        cx, cy = queue.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 <= nx < len(iceberg) and 0 <= ny < len(iceberg[0]):
                if iceberg[nx][ny] > 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

# 빙산이 녹는 과정을 처리하는 함수
def melt_iceberg(iceberg):
    n = len(iceberg)
    m = len(iceberg[0])
    new_iceberg = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] > 0:
                water_count = 0
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0 <= ni < n and 0 <= nj < m and iceberg[ni][nj] == 0:
                        water_count += 1
                new_iceberg[i][j] = max(0, iceberg[i][j] - water_count)
    
    return new_iceberg

def count_iceberg_parts(iceberg):
    n = len(iceberg)
    m = len(iceberg[0])
    visited = [[False] * m for _ in range(n)]
    part_count = 0
    
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited, iceberg)
                part_count += 1
    
    return part_count

def simulate_iceberg(iceberg):
    year = 0
    
    while True:
        parts = count_iceberg_parts(iceberg)
        if parts >= 2:
            return year
        if parts == 0:
            return 0
        
        iceberg = melt_iceberg(iceberg)
        year += 1

# 입력 처리
n, m = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(simulate_iceberg(iceberg))
