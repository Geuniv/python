# 본 코드
S = input()
abc ='abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in S:
        print(S.index(i), end= ' ')
    else:
        print( -1, end =' ')

# 다른 코드
# S = input()
# check = [-1] * 26
#
# for i in range(len(S)):
#     if check[ord(S[i]) - 97] != -1:
#         continue
#     else:
#         check[ord(S[i]) - 97] = i
#
# for i in range(26):
#     print(check[i], end=' ')