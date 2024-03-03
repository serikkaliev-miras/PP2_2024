# 1
# l = list(map(int, input().split()))
# c = 1
# for i in l:
#     c = c * i
# print(c)
# 2
l = list(map(int, input().split()))
print(eval('*'.join(str(i) for i in l)))
