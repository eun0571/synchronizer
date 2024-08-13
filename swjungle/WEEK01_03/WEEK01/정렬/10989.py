import sys

f = [0] * 10000
for i in range(int(sys.stdin.readline())):
    f[int(sys.stdin.readline()) - 1] += 1
for i, cnt in enumerate(f):
    for j in range(cnt):
        print(i + 1)

# def counting_sort(a: list):
#     max_val = max(a)
#     min_val = min(a)
#     range_of_elements = max_val - min_val + 1
#     f = [0] * range_of_elements

#     for i in a:
#         f[i - min_val] += 1

#     a.clear()

#     for i, cnt in enumerate(f):
#         a.extend([i + min_val] * cnt)

#     return a


# def counting_sort(a:list):
#     n = len(a)
#     max_val = max(a)
#     min_val = min(a)
#     range_of_elements = max_val - min_val + 1
#     f = [0] * range_of_elements
#     b = [0] * n

#     for i in range(n):
#         f[a[i] -min_val] += 1
#     for i in range(1,range_of_elements):
#         f[i] += f[i-1]
#     for i in range(n-1, -1, -1):
#         f[a[i]-min_val] -= 1
#         b[f[a[i]-min_val]] = a[i]
#     for i in range(n):
#         a[i]=b[i]
#     return a
