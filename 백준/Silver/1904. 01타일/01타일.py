import sys

n = int(sys.stdin.readline())

a, b = 1, 2
for i in range(2, n):
    a, b = b, (a + b) % 15746
if n == 1:
    print(1)
else:
    print(b)
