import sys

N = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[None] * (1 << N) for _ in range(N)]


def tsp(c_city, v):
    if v == (1 << N) - 1:
        return graph[c_city][0] if graph[c_city][0] else sys.maxsize
    if dp[c_city][v]:
        return dp[c_city][v]
    min_cost = sys.maxsize
    for n_city in range(1, N):
        if not v & 1 << n_city and graph[c_city][n_city]:
            cost = tsp(n_city, v | 1 << n_city) + graph[c_city][n_city]
            min_cost = min(min_cost, cost)
    dp[c_city][v] = min_cost
    return min_cost


print(tsp(0, 1 << 0))
