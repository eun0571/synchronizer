import sys

sys.setrecursionlimit(10**8)
test_case = int(sys.stdin.readline())


def DFS(v, g):
    for i in connect_list[v]:
        if group[i] == None:
            group[i] = (g + 1) & 1
            if not DFS(i, (g + 1) & 1):
                return False
        elif group[i] == g:
            return False
    else:
        return True


for i in range(test_case):
    n, m = map(int, sys.stdin.readline().split())
    # visited = [0 for i in range(n)]
    connect_list = [[] for i in range(n)]
    group = [None for i in range(n)]
    for j in range(m):
        x, y = map(int, sys.stdin.readline().split())
        connect_list[x - 1].append(y - 1)
        connect_list[y - 1].append(x - 1)

    answer = 1
    while None in group:
        v = group.index(None)
        group[v] = 0
        #visited[v] = 1

        if not DFS(v, 0):
            answer = 0
            break
    if answer:
        print("YES")
    else:
        print("NO")
