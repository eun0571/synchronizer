import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

a = deque([i + 1 for i in range(n)])

answer = []

while len(a):
    for i in range(k - 1):
        a.append(a.popleft())
    answer.append(a.popleft())

print(str(answer).replace("[", "<").replace("]", ">"))
