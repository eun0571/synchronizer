import sys

n = int(sys.stdin.readline())

flag_rook = [False for i in range(n)]
flag_bis0 = [False for i in range(2*n-1)]
flag_bis1 = [False for i in range(2*n-1)]

def N_qeen(row):
    comb = 0
    if row == n:
        return 1
    for i in range(n):
        if flag_rook[i] == False and flag_bis0[row+i] == False and flag_bis1[row-i+n-1] == False:
            flag_rook[i] = True
            flag_bis0[row+i] = True
            flag_bis1[row-i+n-1] = True
            comb += N_qeen(row+1)
            flag_rook[i] = False
            flag_bis0[row+i] = False
            flag_bis1[row-i+n-1] = False
    return comb
print(N_qeen(0))
# count = 0
# for i in range(n):
#     count += N_qeen(i)
# print(count)


# k = [(i,j) for i in range(n) for j in range(n)]
# # 결과값만 리턴하는게 중요!! 조합 필요없음
# def pick(l:list,n:int):
#     answer = 0
#     for i in l:
#         reduced = []
#         for j in l[l.index(i)+1:]:
#             if (j[0]!=i[0])and(j[1]!=i[1])and(abs(j[0]-i[0])!=abs(j[1]-i[1])):
#                 reduced.append(j)
#         if n == 2:
#             answer += len(reduced)
#         else:
#             answer += pick(reduced,n-1)
#     return answer
# print(pick(k,n))




# for x in range(n):
#     l = [(0,x)]
    
#     for i in range(1,n): # x
#         for j in range(n): # y
#             if len(l): # 비교 대상 체크
                
#                 for k in range(len(l)): # 개수 만큼 비교
#                     if (l[k][0]!=i) and (l[k][1]!=j): # 룩 비교
#                         m = []
#                         for t in range(1,n): # 비숍비교
#                             m.append((l[k][0]+t,l[k][1]+t))
#                             m.append((l[k][0]-t,l[k][1]+t))
#                             m.append((l[k][0]+t,l[k][1]-t))
#                             m.append((l[k][0]-t,l[k][1]-t))
#                         if (i,j) in m:
#                             break # 비숍 비교 실패
#                         else:pass
#                     else:break # 룩 비교 실패
#                 else: # break 없이 개수 만큼 비교 마치면 가능한 조합
#                     l.append((i,j))
#     else:
#         if len(l) == n:
#             result.append(l)
# print(result)