import re
s = input("")
res = re.split("_", s)
result = res[0] + ''.join(map(lambda x: x.title(), res[1:]))
print(result)
