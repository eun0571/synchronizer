import sys

n = sys.stdin.readline().strip()
result = 0
if n[:2] == "0x":
    my_str = n[:1:-1]
    for i in range(len(my_str)):
        if my_str[i] == "a":
            result += 10 * (1 << (4 * i))
        elif my_str[i] == "b":
            result += 11 * (1 << (4 * i))
        elif my_str[i] == "c":
            result += 12 * (1 << (4 * i))
        elif my_str[i] == "d":
            result += 13 * (1 << (4 * i))
        elif my_str[i] == "e":
            result += 14 * (1 << (4 * i))
        elif my_str[i] == "f":
            result += 15 * (1 << (4 * i))
        else:
            result += int(my_str[i]) * (1 << (4 * i))
elif n[0] == "0":
    my_str = n[:0:-1]
    for i in range(len(my_str)):
        result += int(my_str[i]) * (1 << (3 * i))
else:
    result += int(n)
print(result)
