def gen(a, b):
    for i in range(a, b + 1):
        yield i**2


a, b = int(input()), int(input())
for i in gen(a, b):
    print(i)
