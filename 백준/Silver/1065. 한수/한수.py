import sys

def ishan(a:int):
    A = str(a)
    if len(A) < 3:
        return True
    else:
        for i in range(2,len(A)):
            if int(A[i])-int(A[i-1]) != int(A[1])-int(A[0]):
                break
        else:
            return True
        return False
    
han_count = 0
n = int(sys.stdin.readline())

for i in range(1,n+1):
    if ishan(i):
        han_count += 1

print(han_count)