import sys


def heapify(arr, n, i):
    largest = i
    l = i * 2 + 1
    r = i * 2 + 2
    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if i != largest:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def build_heap(arr, n):
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)


def insert(arr, n, x):
    arr.append(x)
    i = n
    while i > 0 and arr[(i - 1) // 2] < x:
        arr[i], arr[(i - 1) // 2] = arr[(i - 1) // 2], arr[i]
        i = (i - 1) // 2


def remove(arr, n):
    a = arr[0]
    arr[0] = arr[-1]
    arr.pop()
    heapify(arr, n - 1, 0)
    return a


m = int(sys.stdin.readline())

arr = []

for _ in range(m):
    a = int(sys.stdin.readline())

    if a:
        insert(arr, len(arr), a)
    else:
        if not len(arr):
            print(0)
        else:
            print(remove(arr, len(arr)))
