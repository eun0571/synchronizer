import sys

a, b = map(int, sys.stdin.readline().split())
a_list = list(map(int, sys.stdin.readline().split()))
b_list = list(map(int, sys.stdin.readline().split()))
common = 0
print(len(list(set(a_list) - set(b_list))) + len(list(set(b_list) - set(a_list))))
