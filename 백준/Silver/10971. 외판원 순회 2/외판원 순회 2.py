import sys

graph = []
N = int(sys.stdin.readline())
v = 1
c = sys.maxsize
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))


def tsp(n, c_city, c_cost, v):
    global c
    if n == 1:
        if graph[c_city][0]:
            c = min(c, c_cost + graph[c_city][0])
        return
    if c_cost > c:
        return
    for n_city in range(1, N):
        if not v & 1 << n_city and graph[c_city][n_city]:
            tsp(n - 1, n_city, c_cost + graph[c_city][n_city], v | 1 << n_city)

    return


tsp(N, 0, 0, v)
print(c)
