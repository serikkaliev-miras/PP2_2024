def w(f , list):
    try:
        with open(f , 'w') as file:
            for i in list:
                file.write(i + '\n')
list = list(map(str , input().split()))
f = input("")
w(f , list)