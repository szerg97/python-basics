# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# List items are ordered, changeable, and allow duplicate values.
mylist = ["apple", "banana", "cherry"]
print(mylist)
print(len(mylist))

# any data type
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male", False]

# access list items
print(list4[1])
print(list4[-1])
print(list4[2:5])
print(list4[:3])
print(list4[4:])

# check if item exists in list:
thislist = ["apple", "banana", "cherry", "pear", "pineapple"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# change items
thislist[0] = 'plum'
print(thislist)
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist.insert(2, "watermelon")
print(thislist)

# append items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# add any iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# remove list elements
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
