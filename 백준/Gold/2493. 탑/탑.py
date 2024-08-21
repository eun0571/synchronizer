import sys

n = int(sys.stdin.readline())

towers = list(map(int, sys.stdin.readline().split()))
answer = [0] * n
stack = []

for i in range(n):
    while stack and towers[stack[-1]] < towers[i]:
        stack.pop()
    if stack:
        answer[i] = stack[-1]+1
    stack.append(i)
print(' '.join(map(str,answer)))