import sys

input = sys.stdin.readline
t_c = int(input())
for _ in range(t_c):
    n = int(input())
    l = [tuple(map(int, input().split())) for i in range(n)]
    l.sort()
    fail = 0
    max_sec_score = l[0][1]
    for i in range(1, len(l)):
        if l[i][1] < max_sec_score:
            max_sec_score = l[i][1]
            continue
        else:
            fail += 1
    print(len(l) - fail)
