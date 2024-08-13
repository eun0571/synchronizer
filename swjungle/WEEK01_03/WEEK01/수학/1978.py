import sys

n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
prime_count = 0

for i in l:
    div_count = 0
    if i != 1:
        for j in range(1,int(i**0.5)+1):
            div_count += int(i%j==0)
            if div_count > 2:
                break
            else:
                pass
        if div_count == 1:
            prime_count += 1
print(prime_count)