# 1
n = int(input(""))


def fun(n):
    print(28.3495231 * n)


fun(n)

# 2
c = int(input(""))


def f(c):
    print((5 / 9) * (c - 32))


f(c)

# 3
numheads, numlegs = int(input("")), int(input(""))


def solve(numheads, numlegs):
    # print((numlegs / 2) - numheads, numheads - ((numlegs / 2) - numheads))
    a = (numlegs / 2) - numheads
    b = numheads - ((numlegs / 2) - numheads)
    print(int(a), int(b))


solve(numheads, numlegs)

# 4
'''
def prime(n):
    cnt = 0
    for i in range(2, n + 1):
        if n % i == 0:
            cnt = cnt + 1
    return cnt == 2
def filter_prime(m):
    numbers = []
    for n in m:
        if prime(n):
            numbers.append(n)
    return numbers
m = list(map(int, input().split()))
print(filter_prime(m))
'''


def isPrime(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt = cnt + 1
    return cnt == 2


m = list(map(int, input().split()))
print([n for n in m if isPrime(n)])

# 5
'''
from itertools import permutations
str = input("")
permutations_string = list(permutations(str))
print(permutations_string)
'''


def permutate(s):
    p = permutations(s)
    for i in p:
        print(i)


permutate(input("string: "))

# 6
s = input("")


def reverse(s):
    word = s.split()
    return word[::-1]


result = reverse(s)
print(result)
'''
def reverse(sentence):
    word = sentence.split()
    word_r = reversed(word)
    reverse_s = ''.join(word_r)
    return reverse_s


s = input("")
result = reverse(s)

for word in result.split():
    print(word)
'''

# 7


def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False


nums = input("")
l = list(map(int, nums.split()))
result = has_33(l)
print(result)

# 8


def spy_game(nums):
    position = 0
    for num in nums:
        if position == 0 and num == 0:
            position += 1
        elif position == 1 and num == 0:
            position += 1
        elif position == 2 and num == 7:
            return True
    return False


nums = input("")
l = list(map(int, nums.split()))
result = spy_game(l)
print(result)

# 9


def radius(r):
    return 3.14*(3 / 4)*(r**3)


r = int(input(""))
result = radius(r)
print(result)

# 10


def unique(listt):
    newlistt = []
    for element in listt:
        if element not in newlistt:
            newlistt.append(element)
    return newlistt


numbers = input("")
l = list(map(int, numbers.split()))
result = unique(l)
print(result)

# 11


def pal(s):
    return s == s[::-1]


s = input("")
result = pal(s)
print(result)

# 12


def his(my_list):
    for i in range(len(my_list)):
        while my_list[i] > 0:
            print('*', end='')
            my_list[i] -= 1
        print()


numbers = input("")
l = list(map(int, numbers.split()))
result = his(l)
print(result)
