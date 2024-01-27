thistuple = ("apple", "banana", "cherry")
print(thistuple)

# allow duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# tuple with one item
thistuple = ("apple",)
print(type(thistuple))
# NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)

# note the double round-brackets
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
