import sys

n = int(sys.stdin.readline())

l = [i for i in range(1, n + 1)]


def comb(l, n):
    result = []
    if n == 1:
        for i in range(len(l)):
            result.append([l[i]])
    else:
        for i in range(len(l)):
            for j in comb(l[:i] + l[i + 1 :], n - 1):
                result.append([l[i]] + j)
    return result


for i in comb(l, n):
    for j in i:
        print(j, end=" ")
    print("")
