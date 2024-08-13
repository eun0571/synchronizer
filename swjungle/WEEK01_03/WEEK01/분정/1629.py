import sys

sys.setrecursionlimit(10**8)
A, B, C = map(int, sys.stdin.readline().split())


def mod(a, b, c):
    if a == c:
        return 0
    if b == 1:
        return a % c
    else:
        a_ = a % c
        b_ = b // 2
        return mod(a_**2, b_, c) * (a_ if b % 2 else 1) % c


print(mod(A, B, C))
