# List:
# List are ordered collection of data items
# they store multiple items/ multiple datatypes in a single variable
# List items are separated by commas and enclosed by third brackets
# list are changable, we can change after creation


# Ex-1
# lst1 = [1,2,3,4,5,6,7,8,9,10]
# lst2 = ["red","green","blue"]
# print(lst1)
# print(lst2)
#Ex-2
# details = ["Sourav has",18,"chocolates"]
# print(details)

# List index-->List has its own index. Starting form 0 ----> infinity
# We can acess the list data with index value.
# Ex-
# lst3 = [1,"Sourav",3,4,"Mango"]
# print(lst3[2])
# print(lst3[0])
# print(lst3[1])


# Check wheather a color present in the list or not
# colors=["Black", "White", "Gray", "Brown", "Beige"]
# if "yellow" in colors:
#     print("yellow is present")
# else:
#     print("Yellow is absent")
# if "Black" in  colors:
#     print("Black is present")
# else:
#     print("Black is absent")

# list comprehension: for creating new list from other list, tuples, dicts, sets, array, Strings etc

# Syntax----> [Expression(item) for item in iterable if condition]
# Expression: It is which is to be iterable
# Iterable: It can be list, tuples, dicts, array, string, etc.
# Condition: It checks if the item should be added or not

# Accepts the items which starts with "a" in the new list.
# names = ["India","Morocco","Chaina","South America","Austrli","Dubai","Milo"]
# namesWith_a = [item for item in names if "a" in item]
# print(namesWith_a)


# Accept which have more than three characters:
names = ["Milo","Sarah","Bruno","Anastasia","Rosa"]
namesWith_o = [item for item in names if (len(item)>4)]
print(namesWith_o)