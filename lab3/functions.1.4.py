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
