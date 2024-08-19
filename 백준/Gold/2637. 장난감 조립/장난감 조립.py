import sys
from collections import deque

n = int(sys.stdin.readline())

m = int(sys.stdin.readline())

design = [[0 for j in range(n)] for i in range(n)]
in_dgr = [0 for i in range(n)]
graph = [[] for i in range(n)]
for _ in range(m):
    x, y, k = map(int, sys.stdin.readline().split())
    design[x - 1][y - 1] = k
    in_dgr[x - 1] += 1
    graph[y - 1].append(x - 1)


q = deque()
result = {}

is_basic = []


def topological_sort():
    for i in range(n):
        if not sum(design[i]):
            result[i] = 0
        if not in_dgr[i]:
            q.append(i)
    while q:
        v = q.popleft()
        for j in graph[v]:
            in_dgr[j] -= 1
            if in_dgr[j] == 0:
                for sub in range(n):
                    if sub not in result:
                        weight = design[j][sub]
                        design[j][sub] = 0
                        if weight:
                            for k in range(n):
                                design[j][k] += design[sub][k] * weight
                q.append(j)
        if v == n - 1:
            for i in result:
                result[i] = design[v][i]


topological_sort()
for i in result:
    print(i + 1, result[i])
