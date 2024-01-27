# remove == discard  \\ remove IDNE ouput : error , but discard output will not be error
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# if use pop you dont know which item will be remove , because sets - unordered
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)  # removed item
print(thisset)  # the set after removal

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
# output is : set()

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)  # this will raise an error because the set no longer exists
