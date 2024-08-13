l = [6, 4, 3, 7, 1, 9, 8]


# 단순 버블 정렬
def insertion_sort(list):
    n = len(list)

    for i in range(1, n):
        j = i
        tmp = list[i]
        while j > 0 and list[j - 1] > tmp:
            list[j] = list[j - 1]
            j -= 1
        list[j] = tmp


insertion_sort(l)
print(l)
