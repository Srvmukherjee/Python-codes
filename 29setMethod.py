# Set Methods:

# isdisjoint(): This function checks if terms of the items of a given set is present in atother set. 
# if present return false, if not return true.

# name1 = {"Sourav","dipanwita","Saptarshi","Shounak"}
# name2 = {"Sourav","dipanwita","Saptarshi","Shounak"}
# name3 = {"saikat", "Sourin","Sandip","Pratik"}
# print(name1.isdisjoint(name2))
# print(name1.isdisjoint(name3))


# issuperset: It returns true if all the element present in the main set else it return false.
# name1 = {"Sourav","dipanwita","Saptarshi","Shounak"}
# name2 = {"Sourav","Saptarshi","Shounak"}
# name3 = {"saikat", "Sourin","Sandip","Pratik"}
# print(name1.issuperset(name2))
# print(name1.issuperset(name3))

# issubset(): It returns true if the all element of subset present in the main set, else it return false.
# name1 = {"Sourav","Dipanwita","Saptarshi","Sourin"}
# name3 = {"saikat", "Sourin","Sandip","Pratik"}

# print(name2.issubset(name1))
# print(name3.issubset(name1))

# add()- Add of two sets. Adds the elements randomly.
# name1 = {"Sourav","Dipanwita","Saptarshi","Sourin"}
# name1.add("Sandeep")
# print(name1)

# update(): If we want to add more than one item, simply create another set or any other iterable object.
# This method used to add in into the existing sets.
# name1 = {"Sourav","Dipanwita"}
# name2 = {"Saptarshi","Sourin"}

# name1.update(name2)
# print(name1)

# remove or discard:
# name1 = {"Sourav","Dipanwita","Saptarshi","Sourin"}
# name1.discard("Sourav")
# print(name1)

# pop()- Used to remove the last item.
# name1 = {"Sourav","Dipanwita","Saptarshi","Sourin"}
# items = name1.pop()
# print(name1)
# print(items)

# del()- it's not a method, its a keyword for delete the entire set.
# name1 = {"Sourav","Dipanwita","Saptarshi","Sourin"}
# del name1
# print(name1)

# clear()- Clear the whole set and print the empty set.
# name1 = {"Sourav","Dipanwita","Saptarshi","Sourin"}
# name1.clear()
# print(name1)

