import sys

li = set()
for i in range(int(sys.stdin.readline())):
    li.add((sys.stdin.readline()).strip())

for i in sorted(sorted(list(li)),key=lambda x:len(x)):
    print(i)