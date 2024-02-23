import re
s = input("")
# result = []
result = re.findall(r"[A-Z][^A-Z]*", s)
print(result)
