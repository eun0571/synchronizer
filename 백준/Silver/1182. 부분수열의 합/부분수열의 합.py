import sys

n, s = map(int, sys.stdin.readline().split())

l = list(map(int, sys.stdin.readline().split()))
l.sort()


def recur(index, sum):
    if index == n:
        return 1 if sum == s else 0
    return recur(index + 1, sum + l[index]) + recur(index + 1, sum)


result = recur(0, 0)

if s == 0:
    result -= 1
print(result)
