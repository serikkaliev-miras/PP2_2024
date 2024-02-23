import re
s = input("")
lis = re.findall(r"[A-Z][^A-Z]*", s)
result = ' '.join(lis)
print(result)
