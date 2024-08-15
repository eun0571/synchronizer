import sys

sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())

point_set = [tuple(map(int, sys.stdin.readline().split())) for i in range(n)]


def distance_2(a: tuple, b: tuple):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def bruteforce(points):
    n = len(points)
    minst = float('inf')
    for i in range(n - 1):
        for j in range(i + 1, n):
            minst = min(minst, distance_2(points[i], points[j]))
    return minst


def closest_pair(points):
    if len(points) <= 3:
        return bruteforce(points)

    mid = len(points) // 2
    minst = min(closest_pair(points[:mid]), closest_pair(points[mid:]))

    candy = []

    for i in points:
        if (points[mid][0] - i[0]) ** 2 < minst:
            candy.append(i)

    candy.sort(key=lambda x: x[1])

    for i in range(len(candy)):
        for j in range(i + 1, len(candy)):
            if (candy[i][1] - candy[j][1]) ** 2 < minst:
                minst = min(minst, distance_2(candy[i], candy[j]))
            else:
                break
    return minst


if len(point_set) != len(set(point_set)):
    print(0)
else:
    point_set.sort()
    print(closest_pair(point_set))
