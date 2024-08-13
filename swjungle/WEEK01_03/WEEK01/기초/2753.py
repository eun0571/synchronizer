import sys

n = int(sys.stdin.readline())

print(int(bool(not n % 4 and n % 100) or not n % 400))