import sys

n = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))
li.sort()


def binary_search(li, target):
    n = len(li)
    left = 0
    right = n - 1
    while True:
        mid = (left + right) // 2
        if target == li[mid]:
            return mid
        elif target > li[mid]:
            left = mid
        else:
            right = mid
        if left >= right - 1:
            break
    return left


def find_closest(li):

    left = 0
    right = len(li) - 1

    sum = abs(li[0] + li[-1])
    coordi = (0, -1)

    while left < right:
        a = li[left] + li[right]
        if abs(a) < sum:
            sum = abs(a)
            coordi = (left, right)

        if a < 0:
            left += 1
        elif a > 0:
            right -= 1
        else:
            return (li[left], li[right])
    return li[coordi[0]], li[coordi[1]]


if li[0] > 0:
    print(li[0], li[1])
elif li[-1] < 0:
    print(li[-2], li[-1])
else:
    result = find_closest(li)
    print(result[0], result[1])
