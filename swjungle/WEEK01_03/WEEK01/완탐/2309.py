import sys

li=[]

for i in range(9):
    li.append(int(sys.stdin.readline()))

def find(li):
    for i in li:
        for j in li:
            if i!=j:
                lis=li.copy()
                lis.remove(i)
                lis.remove(j)
                if sum(lis) == 100:
                    return lis

for k in sorted(find(li)):
    print(k)