import sys
sys.setrecursionlimit(10**6)

data = list(map(int, sys.stdin.readlines()))

def postorder(start, end):
    if start > end:
        return

    root = data[start]
    idx = start + 1

    while idx <= end:
        if data[idx] > root:
            break
        idx += 1

    postorder(start + 1, idx - 1)  # 왼쪽 서브트리
    postorder(idx, end)            # 오른쪽 서브트리
    print(root)

postorder(0, len(data) - 1)
