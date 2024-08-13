import sys

n, r, c = map(int,sys.stdin.readline().split())

def Z(n,r,c):
    if n == 1:
        return 2*r+c
    i = int(r>=2**(n-1))
    j = int(c>=2**(n-1))
    return 2**(2*n-2)*(2*i+j) + Z(n-1,r-i*2**(n-1),c-j*2**(n-1))

print(Z(n,r,c))