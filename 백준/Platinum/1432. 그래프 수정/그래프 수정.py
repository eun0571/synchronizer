import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())

indgr = [0] * n
graph = [[] for _ in range(n)]

for i in range(n):
    a = list(map(int, sys.stdin.readline().strip()))
    for j in range(n):
        if a[j]:
            graph[j].append(i)
            indgr[i] += 1


heap = []

for i in range(n):
    if indgr[i] == 0:
        heappush(heap, -i)

result = [0] * n
index = n

while heap:

    node = -heappop(heap)
    result[node] = str(index)
    index -= 1
    for i in graph[node]:
        indgr[i] -= 1
        if indgr[i] == 0:
            heappush(heap, -i)
    

if index == 0:
    print(" ".join(result))
else:
    print(-1)
