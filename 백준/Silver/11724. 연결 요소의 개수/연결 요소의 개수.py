import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())

e = []

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    e.append((x - 1, y - 1))

uf = [i for i in range(n)]


def find(x):
    if uf[x] == x:
        return x
    else:
        root = find(uf[x])
        uf[x] = root
        return root


def union(x, y):
    X = find(x)
    Y = find(y)
    uf[X] = Y


def connected_component():
    root_set = set()
    for i in range(m):
        union(e[i][0], e[i][1])
    for i in range(n):
        if find(i) not in root_set:
            root_set.add(uf[i])
    return len(root_set)


print(connected_component())
