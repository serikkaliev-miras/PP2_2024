a = int(input(""))
a3 = a % 10
a2 = (a % 100) // 10
a1 = a // 100
print(str(a) - str(max(a1, a2, a3)) - str(min(a1, a2, a3)))
