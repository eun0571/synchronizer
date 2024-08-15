import sys

a = sys.stdin.readline().strip()

if len(a) == 1:
    a = "0" + a

b = a[1] + str(int(a[0]) + int(a[1]))[-1]
count = 1

while b != a:
    b = b[1] + str(int(b[0]) + int(b[1]))[-1]
    count += 1

print(count)
