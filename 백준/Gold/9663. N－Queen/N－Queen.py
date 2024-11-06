import sys

n = int(sys.stdin.readline())

flag_rook = [False for i in range(n)]
flag_bis0 = [False for i in range(2*n-1)]
flag_bis1 = [False for i in range(2*n-1)]

def N_qeen(row):
    comb = 0
    if row == n:
        return 1
    for i in range(n):
        if flag_rook[i] == False and flag_bis0[row+i] == False and flag_bis1[row-i+n-1] == False:
            flag_rook[i] = True
            flag_bis0[row+i] = True
            flag_bis1[row-i+n-1] = True
            comb += N_qeen(row+1)
            flag_rook[i] = False
            flag_bis0[row+i] = False
            flag_bis1[row-i+n-1] = False
    return comb
print(N_qeen(0))