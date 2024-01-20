x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
print("banana" in x)

x = ["apple", "banana"]
print("pineapple" not in x)

print(6 & 3)  # AND
print(6 | 3)  # OR
print(6 ^ 3)  # XOR
print(~3)  # NOT
print(6 << 3)  # left shift
print(6 >> 3)  # right shift
