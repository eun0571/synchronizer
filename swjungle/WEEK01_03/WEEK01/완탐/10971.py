import sys

N = int(sys.stdin.readline())
matrix = []
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
visited = [0] * N


def TSP(n, start):  # 방문해야하는 도시 개수, 시작도시
    if n == 1:
        if matrix[start][0]:
            visited[0] = 1
            return [matrix[start][0]]
        else:
            return []
    result = []
    # 0(시작 도시)를 제외한 도시를 타겟
    for i in range(1, N):
        if matrix[start][i] and visited[i] == 0:
            visited[i] = 1
            reponse = TSP(n - 1, i)
            if reponse:
                for j in reponse:
                    result.append(j + matrix[start][i])
            visited[i] = 0

    return result


print(sorted(TSP(N, 0))[0])
