import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
A.sort()

M = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))


def exist(n, a, target):
    left = 0
    right = n - 1
    while left <= right:
        h = (right + left) // 2
        if target == a[h]:
            return h
        elif target > a[h]:
            left = h + 1
        else:
            right = h - 1
    return -1


for i in li:
    if exist(N, A, i) == -1:
        print(0)
    else:
        print(1)
