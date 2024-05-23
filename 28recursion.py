# Recursion: Recursion in the process of defining something in terms itself.
# def factorial(num):
#     if(num ==1 or num ==0):
#         return 1
#     else: 
#         return(num *factorial(num-1))

# num = -2
# print("Number:", num)
# print("factorial:",factorial(num))



# Python sets: Sets are unordered collection of data. We can't acess set's elements by index, it stores in unordered manner.
# info={"Sorav",19,False, 3.2121,9.2323}
# print(info)

# 1. joining Sets:
#  union() and update()

name1 = {"Sourav","dipanwita","Saptarshi","Shounak"}
name2 = {"Sourav", "Sourin","Sandip","Pratik"}
name3 = name1.union(name2)                  # Return a new set
print(name3)

name1.update(name2)
print(name1)                                # Adds item to a existing set


# intersection and intersection_update():
name1 = {"Sourav","dipanwita","Saptarshi","Shounak"}
name2 = {"Sourav", "Sourin","Sandip","Pratik"}
name3 = name1.intersection(name2)           # Create a new set
print (name3)

name1.intersection_update(name2)            # This method print only the item present in two sets(Common items)
print(name1)


# symmetric_difference() and symmetric_difference_update():
name1 = {"Sourav","dipanwita","Saptarshi","Shounak"}
name2 = {"Sourav", "Sourin","Sandip","Pratik"}

name3 = name1.symmetric_difference(name2)
print(name3)

name1.symmetric_difference_update(name2)
print(name1)

# difference() and difference_update():
name1 = {"Sourav","dipanwita","Saptarshi","Shounak"}
name2 = {"Sourav", "Sourin","Sandip","Pratik"}

name3 = name1.difference(name2)
print(name3)

name1.difference_update(name2)
print(name1)

