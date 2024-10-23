import sys

n = int(sys.stdin.readline())
result = []
for i in range(2, n + 1):
    while n % i == 0:
        result.append(i)
        n //= i
    if n == 1:
        break
for i in result:
    print(i)
