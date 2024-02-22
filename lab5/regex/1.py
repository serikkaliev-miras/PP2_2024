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
