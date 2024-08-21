import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n)]
reverse_graph = [[] for _ in range(n)]
indgr = [0] * n
dist = [0] * n
visited = [0] * n
for _ in range(m):
    s, d, c = map(int, sys.stdin.readline().split())
    graph[s - 1].append((d - 1, c))
    reverse_graph[d - 1].append((s - 1, c))
    indgr[d - 1] += 1

start, dest = map(int, sys.stdin.readline().split())
start -= 1
dest -= 1


def topological_sort():
    q = deque()

    for i in range(n):
        if indgr[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for next, time in graph[now]:
            if dist[next] < dist[now] + time:
                dist[next] = dist[now] + time
            indgr[next] -= 1
            if indgr[next] == 0:
                q.append(next)


def count_critical_path():
    count = 0
    q = deque([dest])
    visited[dest] = 1
    while q:
        now = q.popleft()
        for prev, time in reverse_graph[now]:
            if dist[now] - time == dist[prev]:
                count += 1
                if not visited[prev]:
                    visited[prev] = 1
                    q.append(prev)
    return count


topological_sort()
path_count = count_critical_path()
print(dist[dest])
print(path_count)
