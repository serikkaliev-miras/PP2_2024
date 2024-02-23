import re
s = input("")
result = re.findall(r"a[a-z]+b\b", s)
print(result)
