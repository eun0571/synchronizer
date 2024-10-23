import sys

n = int(sys.stdin.readline())
my_str = sys.stdin.readline().strip()
result = 0
for i in range(n):
    result += int(my_str[i])
print(result)
