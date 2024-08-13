import sys

a = int(sys.stdin.readline().strip())
b = sys.stdin.readline().strip()

for i in range(1,4):
    print(a*int(b[-i]))

print(a*int(b))