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
