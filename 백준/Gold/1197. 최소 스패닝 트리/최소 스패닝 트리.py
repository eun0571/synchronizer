import sys

sys.setrecursionlimit(10**6)
v, e = map(int, sys.stdin.readline().split())

l = []
for i in range(e):
    x, y, k = map(int, sys.stdin.readline().split())
    l.append((x - 1, y - 1, k))

l.sort(key=lambda x: x[2])

uf = [i for i in range(v)]


def find(x):
    if uf[x] == x:
        return x
    root = find(uf[x])
    uf[x] = root
    return root


def union(x, y):
    X = find(x)
    Y = find(y)
    uf[X] = Y


def kruskal(l):
    result = 0
    for i in l:
        if find(i[0]) != find(i[1]):
            union(i[0], i[1])
            result += i[2]
    return result


print(kruskal(l))
