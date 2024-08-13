import sys

for i in range(int(sys.stdin.readline())):
    a = list(map(int, sys.stdin.readline().split()))
    average = sum(a[1:])/a[0]
    count = 0
    for j in range(a[0]):
        if a[j+1] > average:
            count += 1
    print(f'{count/a[0]*100:.3f}%')