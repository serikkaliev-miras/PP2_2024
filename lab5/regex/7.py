# 1
import re
s = input("")
res = re.split("_", s)
result = res[0] + ''.join(map(lambda x: x.title(), res[1:]))
print(result)
# 2


def test(pattern, testinput, testoutput):
    result = re.sub(pattern, "", testinput)
    if result == testoutput:
        print("test is passed!")
    else:
        print("test is not passed!")


pattern = '[_]'

test(pattern, "Salam_PP1", "SalamPP1")
test(pattern, " Fibo_Itis_Me", " FiboItisMe")
test(pattern, "It_Super_Code", "ItSuperCode")
test(pattern, "It_It_It", "ItItIt")
test(pattern, "Your_Name_Is", "YourNameIs")
