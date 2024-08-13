import sys

n, x = map(int,sys.stdin.readline().split())
for i in map(int,sys.stdin.readline().split()):
    if i < x:
        print(i,end=' ')