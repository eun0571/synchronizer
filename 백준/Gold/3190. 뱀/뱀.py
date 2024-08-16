import sys
from collections import deque

n = int(sys.stdin.readline())


k = int(sys.stdin.readline())
apple_l = []
for i in range(k):
    x, y = map(int, sys.stdin.readline().split())
    apple_l.append((x, y))


l = int(sys.stdin.readline())
dir_l = deque()
for i in range(l):
    t, d = sys.stdin.readline().split()
    dir_l.append((int(t), d))


navi = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction = 0

time = 0

head = (1, 1)
snake = deque([(1, 1)])

while True:
    time += 1
    head = (snake[-1][0] + navi[direction][0], snake[-1][1] + navi[direction][1])

    if not (0 < head[0] < n + 1 and 0 < head[1] < n + 1 and head not in snake):
        break

    snake.append(head)

    if apple_l:
        if head in apple_l:
            apple_l.remove(head)
        else:
            snake.popleft()
    else:
        snake.popleft()

    if dir_l:
        if time == dir_l[0][0]:
            if dir_l[0][1] == "D":
                if direction != 3:
                    direction += 1
                else:
                    direction = 0
            else:
                if direction != 0:
                    direction -= 1
                else:
                    direction = 3
            dir_l.popleft()


print(time)
