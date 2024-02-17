# def even(n):
#     for i in range(n):
#         if i % 2 == 0:
#             yield i
# n = int(input())
# result = even(n)
n = int(input(""))
generator = (i for i in range(1, n) if i % 2 == 0)
even_numbers_str = ', '.join(map(str, generator))
print(even_numbers_str)
