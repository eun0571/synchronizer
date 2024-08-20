import sys
import heapq

n = int(sys.stdin.readline())

l = []
r = []

for i in range(n):
    a = int(sys.stdin.readline())
    if i == 0:
        heapq.heappush(l, -a)
    elif i == 1:
        l_max = -l[0]
        if a < l_max:
            heapq.heappush(r, -heapq.heappop(l))
            heapq.heappush(l, -a)
        else:
            heapq.heappush(r, a)
    else:
        l_max = -l[0]
        r_min = r[0]
        if (i + 1) & 1:
            if a > r_min:
                heapq.heappush(l, -heapq.heappop(r))
                heapq.heappush(r, a)
            else:
                heapq.heappush(l, -a)
        else:
            if a < l_max:
                heapq.heappush(r, -heapq.heappop(l))
                heapq.heappush(l, -a)
            else:
                heapq.heappush(r, a)
    print(-l[0])
