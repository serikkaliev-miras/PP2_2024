def pal(s):
    return s == s[::-1]


s = input("")
result = pal(s)
print(result)
