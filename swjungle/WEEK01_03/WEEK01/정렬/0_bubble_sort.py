l = [6, 4, 3, 7, 1, 9, 8]


# 단순 버블 정렬
def bubble_sort(list):
    for j in range(len(list) - 1):
        for i in range(len(list) - 1, j, -1):
            if list[i] < list[i - 1]:
                list[i - 1], list[i] = list[i], list[i - 1]


# 교환 카운팅 없으면 종료하도록 개선
def bubble_sort_1(list):
    for j in range(len(list) - 1):
        exchng = 0
        for i in range(len(list) - 1, j, -1):
            if list[i] < list[i - 1]:
                list[i - 1], list[i] = list[i], list[i - 1]
                exchng += 1
        if not exchng:
            break


def bubble_sort_2(list):
    n = len(list)
    k = 0
    while k < n - 1:
        last = n - 1
        for i in range(n - 1, k, -1):
            if list[i] < list[i - 1]:
                list[i - 1], list[i] = list[i], list[i - 1]
                last = i
        k = last


def shaker_sort(list):
    n = len(list)
    left = 0
    right = n - 1
    last = right

    while left < right:
        for i in range(right, left, -1):
            if list[i] < list[i - 1]:
                list[i - 1], list[i] = list[i], list[i - 1]
                last = i
        left = last

        for i in range(left, right, 1):
            if list[i] < list[i - 1]:
                list[i - 1], list[i] = list[i], list[i - 1]
                last = i
        right = last


shaker_sort(l)
print(l)
