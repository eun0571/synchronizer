import sys

n = int(sys.stdin.readline())
word = sys.stdin.readline().strip()

hidden = ""
result = 0

for i in word:
    if ord(i) >= 65:
        if 0 < len(hidden) <= 6:
            result += int(hidden)
        hidden = ""
    else:
        hidden += i
if hidden:
    print(result + int(hidden))
else:
    print(result)
