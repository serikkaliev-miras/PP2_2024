# import re
# s = input("")
# l = re.findall(r'[A-Z][a-z]+', s)
# list = []
# for i in l:
#     i = i.lower()
#     list.append(i)
# print(list)

import re
s = input("")
l = re.findall(r'[A-Z][a-z]+', s)
result = '_'.join([x.lower() for x in l])
print(result)
