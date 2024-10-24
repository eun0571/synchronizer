import sys

n = sys.stdin.readline().strip()

for i in range(1, int(n)):
    a = 0
    for j in range(len(str(i))):
        a += int(str(i)[j])
    if i + a == int(n):
        print(i)
        break
else:
    print(0)
