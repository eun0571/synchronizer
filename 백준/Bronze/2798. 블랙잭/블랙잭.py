import sys

n, m = map(int, sys.stdin.readline().split())

li = sorted(map(int, sys.stdin.readline().split()))
sum_li = set()

def blackJ(n, m, li):
    for i in range(n):
        if li[i] < m:
            for j in range(i + 1, n):
                if li[j] < m - li[i]:
                    for k in range(j + 1, n):
                        if li[k] <= m - li[i] - li[j]:
                            sum_li.add(li[i] + li[j] + li[k])


blackJ(n, m, li)

print(sorted(list(sum_li))[-1])