import sys

for i in range(int(sys.stdin.readline())):
    re, string = sys.stdin.readline().split()
    for j in string:
        print(j*int(re),end='')
    print()