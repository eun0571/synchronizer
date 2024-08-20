import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())

# 구슬 관계를 나타내는 그래프
heavier = [[] for _ in range(n)]
lighter = [[] for _ in range(n)]

# 입력 처리
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    heavier[a].append(b)  # a가 b보다 무겁다
    lighter[b].append(a)  # b가 a보다 가볍다

# DFS 함수 정의
def dfs(node, graph, visited):
    count = 0
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            count += 1 + dfs(next_node, graph, visited)
    return count

result = 0

# 모든 구슬에 대해 무게를 비교
for i in range(n):
    visited = [False] * n
    
    heavy_count = dfs(i, heavier, visited)
    light_count = dfs(i, lighter, visited)
    
    if heavy_count > n // 2 or light_count > n // 2:
        result += 1

print(result)
