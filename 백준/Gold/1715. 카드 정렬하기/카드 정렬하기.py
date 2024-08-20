import sys
import heapq

n = int(sys.stdin.readline())

l = []
for _ in range(n):
    l.append(int(sys.stdin.readline()))

heapq.heapify(l)

result = 0
for _ in range(n - 1):
    a = heapq.heappop(l)
    b = heapq.heappop(l)
    result += a + b
    heapq.heappush(l, a + b)

print(result)
