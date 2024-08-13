import sys

for i in range(int(sys.stdin.readline())):
    answer = 0
    acc = 1
    for j in range(len(my_str:=sys.stdin.readline().strip())):
        if my_str[j] == 'O':
            answer += acc
            acc += 1
        else:
            acc = 1
    print(answer)