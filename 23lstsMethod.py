# List Methods:
# list.sort() - for sort the list in acending order
list = [1,2,3,5,6,8,3,2,7,9,32,2,3,5,63,63,2]
list.sort()
print(list)


# For decending order list.sort(reverse=True)
list1 = [1,2,3,5,6,8,3,2,7,9,32,2,3,5,63,63,2]
list1.sort(reverse=True)
print(list1)


#reverse() --> For reverse the order of the list.
list = [1,2,3,5,6,8,3,2,7,9,32,2,3,5,63,63,2]
list.reverse()
print(list)


# index() -->return the index of first occurance of the list item
list1 = [1,2,3,5,6,8,3,2,7,9,32,2,3,5,63,63,2]
list2 = ["Red", "Green", "Blue", "Yellow", "Orange"]

print(list2.index("Green"))
print(list1.index(32))



#count()---> Return count of the number with the given value
list2 = ["Red", "Yellow", "Blue", "Yellow", "Orange"]
print(list2.count("Yellow"))
print(list2.count("Red"))

#copy()---> Return the copy of the list.
list2 = ["Red", "Yellow", "Blue", "Yellow", "Orange"]
list3 = list2.copy()
print(list3)

#append() ---> this method append items to the end of existing list.
list2 = ["Red", "Yellow", "Blue", "Yellow", "Orange"]
list2.append("Black")
print(list2)

# insert()---> this method used to add an item in a given index.
list2 = ["Red", "Yellow", "Blue", "Yellow", "Orange"]
list2.insert(2,"Sky blue")
print(list2)


#extends()--> this method add entire list or any other collection datatypes to the existing list.
list1 = [1,2,3,5,6,8,3,2,7,9,32,2,3,5,63,63,2]
list2 = ["Red", "Yellow", "Blue", "Yellow", "Orange"]
list1.extend(list2)
print(list1)


# Concentrating two lists
list1 = [1,2,3,5,6,8,3,2,7,9,32,2,3,5,63,63,2]
list2 = ["Red", "Yellow", "Blue", "Yellow", "Orange"]
print(list1+list2)