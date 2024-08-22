import sys
from collections import deque
from heapq import heappop, heappush

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n)]
indgr = [0 for _ in range(n)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a - 1].append(b - 1)
    indgr[b - 1] += 1

heap = []

for i in range(n):
    if not indgr[i]:
        heappush(heap, i)
    graph[i].sort()

result = []

while heap:
    now = heappop(heap)
    result.append(now + 1)
    for sub in graph[now]:
        indgr[sub] -= 1
        if not indgr[sub]:
            heappush(heap, sub)

print(" ".join(map(str, result)))
