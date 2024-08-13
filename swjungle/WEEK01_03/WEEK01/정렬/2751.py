import sys

li = []

for i in range(int(sys.stdin.readline())):
    li.append(int(sys.stdin.readline()))

li.sort()

for i in li:
    print(i)