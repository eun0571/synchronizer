import sys

f = [0] * 10000
for i in range(int(sys.stdin.readline())):
    f[int(sys.stdin.readline())-1] += 1
for i, cnt in enumerate(f):
    for j in range(cnt):
        print(i+1)