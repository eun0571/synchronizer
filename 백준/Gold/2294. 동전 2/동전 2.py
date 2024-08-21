from collections import deque
import sys

input = sys.stdin.readline

# 입력 받기
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# 방문 여부와 최소 동전 개수 기록을 위한 리스트
visited = [False] * (k + 1)
dist = [-1] * (k + 1)
dist[0] = 0  # 0원을 만드는 데 필요한 동전 개수는 0개

# BFS를 위한 큐 초기화
queue = deque([0])

while queue:
    current = queue.popleft()

    for coin in coins:
        next_value = current + coin

        if next_value > k:
            continue

        if not visited[next_value]:
            visited[next_value] = True
            dist[next_value] = dist[current] + 1
            queue.append(next_value)

# 결과 출력
print(dist[k])
