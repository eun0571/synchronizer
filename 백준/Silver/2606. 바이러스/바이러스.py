import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

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
    for i in range(m):
        union(e[i][0], e[i][1])
    root_1 = find(0)
    result = 0
    for i in range(1, n):
        if find(i) == root_1:
            result += 1
    return result


print(connected_component())
