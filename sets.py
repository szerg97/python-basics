# Set items are unchangeable, but you can remove items and add new items.
# Sets are unordered, so you cannot be sure in which order the items will appear.
# Sets cannot have two items with the same value.

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# True = 1 -> duplicates!!
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# False = 0 -> duplicates!!
thisset = {"apple", "banana", "cherry", False, 0, 2}
print(thisset)

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}

# add
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# remove (if the item does not exist, it will raise an error)
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# remove (if the item does not exist, it will NOT raise an error)
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset2 = {"apple", "banana", "cherry"}
del thisset2
print(thisset2)
