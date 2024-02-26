# # 1
import re
with open("row.txt") as file:
    lines = file.readlines()
for i in lines:
    result = re.findall("a(b*)", i)
    print(result)

# # 2
l = input("")
need = re.findall(r"a(b*)", l)
if need:
    print("yes")
else:
    print("no")

# 3
s = input("")
result = re.findall(r"^a(b*)$", s)
if result:
    print("yep")
else:
    print("no")

# 3


def test(pattern, testinput, testoutput):
    if re.search(pattern, testinput) == testoutput:
        print("test is not passed")
    elif re.search(pattern, testinput) != None:
        print("test is passed!")
    else:
        print("test is not passed")


pattern = '^a(b*).'

test(pattern, "123ab45", None)
test(pattern, "123ab45as", None)
test(pattern, "123ab452", None)
test(pattern, "abb", True)
test(pattern, "abbb452", True)
