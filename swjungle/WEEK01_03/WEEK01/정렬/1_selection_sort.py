l = [6, 4, 3, 7, 1, 9, 8]


# 단순 버블 정렬
def selection_sort(list):
    n = len(list)

    for i in range(n):
        min_dex = i
        for j in range(i, n):
            if list[j] < list[min_dex]:
                min_dex = j

        list[min_dex], list[i] = list[i], list[min_dex]


selection_sort(l)
print(l)
