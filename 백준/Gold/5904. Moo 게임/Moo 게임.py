import sys

sys.setrecursionlimit(10**8)
n = int(sys.stdin.readline())


def target_k(n):
    m = 0
    moo_len = 3
    while n > moo_len:
        moo_len = 2 * moo_len + m + 4
        m += 1
    return m, moo_len


def recur(k, moo_len, n):
    if k == 0:
        if n == 1:
            return "m"
        else:
            return "o"
    sub_len = (moo_len - k - 3) // 2
    if n <= sub_len:
        return recur(k - 1, sub_len, n)
    elif n == sub_len + 1:
        return "m"
    elif sub_len + 1 < n <= sub_len + k + 3:
        return "o"
    else:
        return recur(k - 1, sub_len, n - sub_len - k - 3)


m, moo_len = target_k(n)

print(recur(m, moo_len, n))

# a = target_k(n)
# print(recur(a, n, moo_len(a)))
