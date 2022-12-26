#Creating an empty set
b = set()
print(type(b))

#Adding values to an empty set
b.add(4)
b.add(5)
b.add(6) #cannot add list or dictionary inside sets.
print(b)

print(len(b)) #prints the length of this set.

#Removal of an item
b.remove(5) #removes the particular element from the set.
print(b)

print(b.pop())


