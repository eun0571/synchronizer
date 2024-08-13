import sys

N = int(sys.stdin.readline())

matrix = []
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))


def is_uniform(n, i_start, j_start):
    initial = matrix[i_start][j_start]
    for i in range(i_start, i_start + n):
        for j in range(j_start, j_start + n):
            if matrix[i][j] != initial:
                return False, initial
    return True, initial


def divide_conquer(n, i_start=0, j_start=0):

    half = n // 2
    uniform, value = is_uniform(n, i_start, j_start)
    zero = 0
    one = 0
    if uniform:
        return [0, 1] if value else [1, 0]
    else:
        for i in range(2):
            for j in range(2):
                count = divide_conquer(half, half * i + i_start, half * j + j_start)
                zero += count[0]
                one += count[1]

    return [zero, one]


print(divide_conquer(N)[0])
print(divide_conquer(N)[1])
