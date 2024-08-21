import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
places = list(map(int, input().strip()))  # 1이면 실내, 0이면 실외
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)

# 실내와 실내를 직접 연결하는 경로를 찾기
indoor_paths = 0
for i in range(1, n + 1):
    if places[i - 1] == 1:
        for neighbor in graph[i]:
            if places[neighbor - 1] == 1:
                indoor_paths += 1

# 실내-실외-실내 경로를 찾기
visited = [False] * (n + 1)


def bfs(start):
    queue = deque([start])
    visited[start] = True
    indoor_count = 0

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if places[neighbor - 1] == 1:
                indoor_count += 1
            if not visited[neighbor] and places[neighbor - 1] == 0:
                visited[neighbor] = True
                queue.append(neighbor)

    return indoor_count * (indoor_count - 1)


outdoor_paths = 0
for i in range(1, n + 1):
    if not visited[i] and places[i - 1] == 0:
        outdoor_paths += bfs(i)

result = indoor_paths + outdoor_paths
print(result)
