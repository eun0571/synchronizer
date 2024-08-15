import sys

m, n, l = map(int, sys.stdin.readline().split())

x = list(map(int, sys.stdin.readline().split()))
x.sort()
ani = [tuple(map(int, sys.stdin.readline().split())) for i in range(n)]


def binary_search(li_x, t, m):
    n_x = m
    left = 0
    right = n_x - 1
    while left <= right:
        mid = (left + right) // 2
        if t == li_x[mid]:
            return mid
        elif t > li_x[mid]:
            left = mid + 1
        else:
            right = mid - 1
    if left == n_x:
        return right
    elif right == -1:
        return left
    else:
        if t - li_x[right] < li_x[left] - t:
            return right
        else:
            return left


def solution(li_ani, li_x, l_rip, m, n):
    count = 0
    for i in range(n):
        x_index = binary_search(li_x, li_ani[i][0], m)
        if abs(li_x[x_index] - li_ani[i][0]) + li_ani[i][1] <= l_rip:
            count += 1
    return count


print(solution(ani, x, l, m, n))
