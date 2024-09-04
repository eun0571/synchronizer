import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
n = int(input())
graph = [[0 for j in range(n)] for i in range(n)]
for i in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c

result = 0
visited = [0 for _ in range(n)]
visited[0] = 1


def dfs(start, distance):
    global result
    last_flag = 1
    for i in range(n):
        if graph[start][i] and not visited[i]:
            visited[i] = 1
            dfs(i, distance + graph[start][i])
            visited[i] = 0
            last_flag = 0
    if last_flag:
        result = max(distance, result)


dfs(0, 0)

print(result)
