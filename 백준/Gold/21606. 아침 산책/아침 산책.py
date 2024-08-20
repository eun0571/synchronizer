import sys

n = int(sys.stdin.readline())

indoor = sys.stdin.readline().strip()
indoor = [int(indoor[i]) for i in range(n)]
c_l = [[] for _ in range(n)]

for _ in range(n - 1):
    x, y = map(int, sys.stdin.readline().split())
    c_l[x - 1].append(y - 1)
    c_l[y - 1].append(x - 1)


def walk(start):
    answer = 0
    for i in c_l[start]:
        if not visited[i]:
            visited[i] = 1
            if indoor[i]:
                answer += 1
            else:
                answer += walk(i)
    return answer


result = 0
for i in range(n):
    visited = [0 for _ in range(n)]
    if indoor[i]:
        visited[i] = 1
        result += walk(i)

print(result)
