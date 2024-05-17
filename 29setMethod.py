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
# name2 = {"Saptarshi","Sourin"}
# name3 = {"saikat", "Sourin","Sandip","Pratik"}

# print(name2.issubset(name1))
# print(name3.issubset(name1))

# add()- Add of two sets.
name1 = {"Sourav","Dipanwita","Saptarshi","Sourin"}
name1.add("Sandeep")
print(name1)
