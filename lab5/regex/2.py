import re
s = input("")
result = re.findall(r"ab{2,3}", s)
if result:
    print(result)
else:
    print("no")
