import sys
from heapq import heappush, heappop

input = sys.stdin.readline
n = int(input())
l = []
for i in range(n):
    k, start, end = map(int, input().split())
    l.append((end, start, k - 1))
l.sort(key=lambda x: x[1])

heap = [l[0]]
room = [0 for i in range(n)]
room[l[0][2]] = 1
answer = 1
for i in range(1, n):
    if heap[0][0] <= l[i][1]:
        room[l[i][2]] = room[heap[0][2]]
        heappop(heap)
    else:
        answer += 1
        room[l[i][2]] = answer
    heappush(heap, l[i])
print(answer)
for i in room:
    print(i)
