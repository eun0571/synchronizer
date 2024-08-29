import sys

input = sys.stdin.readline
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
for i in l:
    print(min(i))
