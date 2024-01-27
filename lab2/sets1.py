# set{} , tuple() , list[]

thisset = {"apple", "banana", "cherry"}
print(thisset)

# sets doesnt have duplicates, and we cant use index because its unordered
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# true and 1 the same value , so False and 0 the same, also
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

set1 = {"abc", 34, True, 40, "male"}
print(set1)

thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)
