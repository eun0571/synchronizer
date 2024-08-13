import sys

n = int(sys.stdin.readline())

def move_count(n):
    return 1 if n == 1 else 2*move_count(n-1)+1

print(move_count(n))

def move(n,start,empty,goal):
    if n == 1:
        print(start, goal)
    else:
        move(n-1,start,goal,empty)
        move(1,start,empty,goal)
        move(n-1,empty,start,goal)

if n <= 20:
    move(n,'1','2','3')

# 메모리 초과
# def move(n,start,empty,goal):
#     if n == 1:
#         return [start+' '+goal]
#     else:
#         return move(n-1,start,goal,empty)+move(1,start,empty,goal)+move(n-1,empty,start,goal)
    
# result = move(n,'1','2','3')

# print(len(result))
# for i in result:
#     print(i)