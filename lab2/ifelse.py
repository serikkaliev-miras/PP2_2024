a = 33
b = 200
if b > a:
    print("b is greater than a")

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

if a > b:
    print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")  # ternary operators
print("A") if a > b else print("=") if a == b else print(
    "B")  # multiple else statements

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")  # there are exists or

a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

# nested if
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

a = 33
b = 200
if b > a:
    pass
# having an empty if statement like this, would raise an error without the pass statement
