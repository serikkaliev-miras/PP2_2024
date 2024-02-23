import re
s = input("")
result = re.findall(r"[a-z]_[a-z]", s)
print(result)
