import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

l = []

for i in range(n):
    l.append(sys.stdin.readline().strip())

def put_down(a:list,b:int,c:str):
    result = []
    if b == 1:
        for i in range(len(a)):
            result.append(c+a[i])
    else:
        for i in range(len(a)):
            result += put_down((a*2)[i+1:i+len(a)],b-1,c+a[i])
    return result

result = put_down(l,k,'')

print(len(set(result)))