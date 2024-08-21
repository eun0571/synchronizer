def solve():
    string = input().strip()
    bomb = input().strip()
    stack = []
    bomb_len = len(bomb)
    
    for char in string:
        stack.append(char)
        if len(stack) >= bomb_len and ''.join(stack[-bomb_len:]) == bomb:
            del stack[-bomb_len:]
    
    result = ''.join(stack)
    print(result if result else "FRULA")

solve()