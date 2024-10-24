import sys

text = sys.stdin.readline().strip()
n = int(sys.stdin.readline())

left = []
right = []

for i in range(len(text)):
    left.append(text[i])

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "L":
        if left:
            right.append(left.pop())
    elif command[0] == "D":
        if right:
            left.append(right.pop())
    elif command[0] == "P":
        left.append(command[1])
    elif left:
        left.pop()

print("".join(left) + "".join(right[::-1]))
