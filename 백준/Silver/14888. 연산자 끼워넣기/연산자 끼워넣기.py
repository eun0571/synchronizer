import sys

N = int(sys.stdin.readline())

l = list(map(int, sys.stdin.readline().split()))

op = list(map(int, sys.stdin.readline().split()))

op_set = ["+", "-", "*", "//"]

used_op = [0, 0, 0, 0]


# 뒤에서부터 연산자 놓는다고 생각
def insert_op(n: int):  # 사용 가능한 연산자 개수, 앞의 연산 결과값
    if n == 0:
        return [l[0]]
    else:
        answer = []
        for i in range(4):
            if used_op[i] < op[i]:
                used_op[i] += 1
                prev_result = insert_op(n - 1)
                for j in prev_result:
                    if j < 0 and i == 3:
                        answer.append(eval(str(abs(j)) + op_set[i] + str(l[n])) * (-1))
                    else:
                        answer.append(eval(str(j) + op_set[i] + str(l[n])))
                used_op[i] -= 1
    return answer


print(sorted(insert_op(N - 1))[-1])
print(sorted(insert_op(N - 1))[0])