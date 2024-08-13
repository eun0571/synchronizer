import sys

n = 1

for i in range(3):
    n *= int(sys.stdin.readline())
for i in range(10):
    print(str(n).count(str(i)))