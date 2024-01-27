thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# [i:j] -> i - inclusive , j - not inclusive..
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
# output :  ["apple", "banana", "watermelon" ,"cherry"]
