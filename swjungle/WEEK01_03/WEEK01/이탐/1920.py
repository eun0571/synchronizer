import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
a.sort()

m = int(sys.stdin.readline())

b = list(map(int, sys.stdin.readline().split()))


def exist(n, a, m, b):
    for i in range(m):
        left = 0
        right = n
        h = (right - left) // 2
        while left < right - 1:
            print(left, right, b[i])
            if b[i] > a[h]:
                left = h + 1
            elif b[i] < a[h]:
                right = h
            else:
                break
            h = (right - left) // 2
        if a[h] == b[i]:
            print(1)
        else:
            print(0)


exist(n, a, m, b)
