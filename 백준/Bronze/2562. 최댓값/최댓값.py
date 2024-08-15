import sys

item_list=[]

for i in range(9):
    item_list.append(int(sys.stdin.readline()))
print(max(item_list))
print(item_list.index(max(item_list))+1)