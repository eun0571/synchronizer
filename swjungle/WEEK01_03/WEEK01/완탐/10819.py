import sys

n = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))


def solution(n, li):
    if n == 1:
        return [li]
    answer = []
    for i in range(n):
        for j in solution(n - 1, li[:i] + li[i + 1 :]):
            answer.extend([[li[i]] + j])
    return answer


result = []
for i in solution(n, li):
    a = 0
    for j in range(1, n):
        a += abs(i[j] - i[j - 1])
    result.append(a)
print(max(result))
