import sys
import heapq

n = int(sys.stdin.readline())

l = []
for _ in range(n):
    h, o = map(int, sys.stdin.readline().split())
    l.append(tuple((min(h, o), max(h, o))))

distance = int(sys.stdin.readline())

l.sort(key=lambda x: x[1])

heap = []
max_count = 0
for i in l:
    start, end = i
    heapq.heappush(heap, start)

    while heap and heap[0] < end - distance:
        heapq.heappop(heap)

    max_count = max(max_count, len(heap))

print(max_count)
