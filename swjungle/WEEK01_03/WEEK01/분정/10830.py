import sys

# 입력을 받습니다.
n, b = map(int, sys.stdin.readline().split())
matrix_a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 단위 행렬을 생성합니다.
identity_matrix = [[1 if i == j else 0 for i in range(n)] for j in range(n)]


def matrix_multiplication(x, y):
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            element = 0
            for k in range(n):
                element += x[i][k] * y[k][j]
            row.append(element % 1000)
        result.append(row)
    return result


def matrix_exponentiation(matrix, exp):
    if exp == 1:
        return matrix_multiplication(matrix, identity_matrix)
    half_exp_result = matrix_exponentiation(
        matrix_multiplication(matrix, matrix), exp // 2
    )
    if exp % 2 == 0:
        return half_exp_result
    else:
        return matrix_multiplication(half_exp_result, matrix)


# 행렬의 b 제곱을 계산합니다.
result_matrix = matrix_exponentiation(matrix_a, b)

# 결과를 출력합니다.
for row in result_matrix:
    print(" ".join(map(str, row)))
