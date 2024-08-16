import sys
from collections import deque

n = int(sys.stdin.readline())

tree = deque()

for i in range(n):
    tree.append(int(sys.stdin.readline()))

count = 1
height = tree[-1]
for i in range(len(tree) - 1, -1, -1):
    if tree[i] > height:
        count += 1
        height = tree[i]
print(count)
