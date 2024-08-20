import sys

m = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
op = ["+", "-", "*", "//"]
remain = list(map(int, sys.stdin.readline().split()))

result = []


def DFS(n):
    if n < 1:
        return [l[0]]
    answer = []
    for i in range(4):
        if remain[i]:
            remain[i] -= 1
            for j in DFS(n - 1):
                if j < 0 and i == 3:
                    answer.append(-eval(f"{-j}{op[i]}{l[n]}"))
                else:
                    answer.append(eval(f"{j}{op[i]}{l[n]}"))
            remain[i] += 1
    return answer


result = DFS(m - 1)
print(max(result))
print(min(result))
