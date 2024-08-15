import sys

def isprime(a):
    div_count = 0
    if a != 1:
        for i in range(1,int(a**0.5)+1):
            div_count += int(a%i==0)
            if div_count > 1:
                return False
        return True
    else:
        return False

for i in range(int(sys.stdin.readline())):
    a = (n:=int(sys.stdin.readline()))//2
    while not isprime(a) or not isprime(n-a):
        a -=1
    print(a,n-a)