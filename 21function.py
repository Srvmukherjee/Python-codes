# FUNCTION: A function is a block of code that performs a specifiv task whenever it called

# There are two types of function:
# 1. Built in Function
# 2. User defined Function

# 1. Built in Function: These funtion are defined and precoded in python. 
# min()
# max()
# len()
# sum()
# type()
# range()
# dict()
# list()
# tuple()
# set()
# print()


# User defined Function: We can create function to perform specific task. we called this user defined function.

#syntax:
# def function_name(parameters):
#     pass
# code and statements

# Create a function using the def keyword, followed by the function name, followed by a parenthysis and colon.





#Calling function:
# def name(fname, lname):
#     print("Hello", fname,lname)

# name("Sam","Wilson")



#FUNCTION ARGUMENT:
# 1. Defalut argument
# 2. Keyword argument
# 3. Variable length arguement
# 4. Required Argument.

# 1. Default argument: we can provide defalut value whhile creating a function.

# def name(fname, mname = "Jhon",lname = "Whatson"):
#     print("Hello,",fname,mname,lname)
# name("Amy")


# 2. Keyword argument: We can provide with key == value, for recognize argument

# def name(fname,mname, lname):
#     print("Hello,",fname,mname,lname)
# name(mname="kumar",lname = "Mukherjee", fname = "Sourav")

# 3. Required Arguments: in this case we don't pass the argument with the key = value syntax,then it necessary to pass the arguments in the corect positional order the number of argument passed should match with actual number of arguments.

# Example 1: when the number of argument dont match with the actual function definition
# def name(fname, mname,lname):
#     print("Hello",fname,mname,lname)
# name("peter","Quill")     ----> Type error.

# def name(fname,mname,lname):
#     print("Hello,",fname,mname,lname)

# name("Sourav","Kumar","Mukherjee")

# 4. Variable length arguments: Sometimes we may need to pass more argument than those defined in actual arguments
# i. Arbitary Arguments: while creating a function if we add * before the paramenter then the paramenter agrument processing them in the form of tuple.
# def name(*name):
#     print("Hello,",name[0],name[1],name[2])
# name("Sourav","Sourin","Sandeep")

# ii. Keyword Arbitary arguments: while creating a function pass ** before the paramenter namee while define the functiion, the function acesses the arguments by processing them in the form of dictnary.
# def name(**name):
#     print("Hello,",name["fname"],name["mname"],name["lname"])
# name(mname="Buchanan",fname="sourab",lname="Kumar")


# Return Statement: This is used to return the value of the expression back to the calling function
def name(fname,mname,lname):
    return "hello,"+fname+" "+mname+" "+lname
print(name("james","lorence","bishnoi"))
