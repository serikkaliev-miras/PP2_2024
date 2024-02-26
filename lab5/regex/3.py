import re
s = input("")
result = re.findall(r"[a-z]_[a-z]", s)
print(result)
 #3
 import re

def test(pattern, testinput, expectedResult):
    if re.search(pattern, testinput) == expectedResult:
        print("test is passed!")
    elif re.search(pattern, testinput) != None:
        print("test is passed")
    else: 
        print("test is not passed!")

pattern = '[a-z]_[a-z]'
test(pattern, "aa_bb_cc", True)
test(pattern, "a_b_c", None)
test(pattern, "abbb(*452", None)
test(pattern, "123a_b45", True)
test(pattern, "123a_b45as", True) 