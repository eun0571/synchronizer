import sys
a,b,v = map(int,sys.stdin.readline().split())

print((v-a)//(a-b)+((v-a)%(a-b)!=0)+1)