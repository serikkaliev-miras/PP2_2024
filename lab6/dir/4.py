def count(f):
    try:
        with open(f , 'r') as file:
            lines = file.readlines()
            n = len(lines)
            return n
f = input("")
l = count(f)
print(l)