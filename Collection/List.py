thislist = ["apple", "banana", "cherry"]

print(thislist)
print(thislist[1])

thislist[1] = "blackcurrant"
print(thislist)

# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Check if Item Exists
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# List Length
print(len(thislist))

# Add Items
thislist.append("orange")
print(thislist)

# Insert an item as the second position:
thislist.insert(1, "orange 2.0")
print(thislist)

# Remove Item
thislist.remove("banana")
print(thislist)

# The pop() method removes the specified index, (or the last item if index is not specified):
thislist.pop()
print(thislist)

# The del keyword removes the specified index:
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely:
thislist2 = ["apple", "banana", "cherry"]
del thislist2
# print(thislist2)

# The clear() method empties the list:
thislist3 = ["apple", "banana", "cherry"]
#thislist3.clear()
#print(thislist3)

# The list() Constructor
thislist4 = list(("BD", "JP", "USA")) # note the double round-brackets
print(thislist4)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

















