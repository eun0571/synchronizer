import sys

sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())

point_set = [tuple(map(int, sys.stdin.readline().split())) for i in range(n)]
point_set.sort(key=lambda x: x[0] + x[1])


def distance_2(a: tuple, b: tuple):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def divide_plane(points):
    n = len(points)

    if n == 1:
        return 400000000
    if n == 2:
        d = distance_2(points[0], points[1])
        if d == 1:
            print(d)
        return distance_2(points[0], points[1])
    if n == 3:
        return min(
            distance_2(points[0], points[1]),
            distance_2(points[1], points[2]),
            distance_2(points[2], points[0]),
        )
    if n == 4:
        return min(
            distance_2(points[0], points[1]),
            distance_2(points[0], points[2]),
            distance_2(points[0], points[3]),
            distance_2(points[1], points[2]),
            distance_2(points[1], points[3]),
            distance_2(points[2], points[3]),
        )

    for i in points:
        points_1 = []
        points_2 = []
        points_3 = []
        points_4 = []
        for j in points:
            if j[0] <= i[0]:
                if j[1] <= i[1]:
                    points_3.append(j)
                if j[1] >= i[1]:
                    points_2.append(j)
            if j[0] >= i[0]:
                if j[1] >= i[1]:
                    points_1.append(j)
                if j[1] <= i[1]:
                    points_4.append(j)
        if (
            (points_1 == points)
            or (points_2 == points)
            or (points_3 == points)
            or (points_4 == points)
        ):
            pass
        else:
            return min(
                divide_plane(points_3),
                divide_plane(points_2),
                divide_plane(points_4),
                divide_plane(points_1),
            )
    else:
        raise


if len(point_set) != len(set(point_set)):
    print(0)
else:
    print(divide_plane(point_set))
