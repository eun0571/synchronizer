import sys

sys.setrecursionlimit(10**8)
n, c = map(int, sys.stdin.readline().split())

l = [int(sys.stdin.readline()) for i in range(n)]
l.sort()

start_target = (l[-1] - l[0]) // (c - 1)


def target_binary_search(start, li, c):
    left = 1
    right = start
    while left <= right:
        target = (left + right) // 2
        if check_possibility(li, target, c):
            left = target + 1
        else:
            right = target - 1
    return right


def check_possibility(li, target, c):
    count = 1
    last_installed = 0

    for i in range(1, len(li)):
        if li[i] >= li[last_installed] + target:
            last_installed = i
            count += 1
            if count>=c:
                return True
    return False

print(target_binary_search(start_target, l, c))
