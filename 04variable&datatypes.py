# Variable is a container which stores data
# Data types specify the type of value a variable can store

#Example of variables:
a=1
b=True
c="Sourav"
d=None


#Examples of datatypes:
print(type(a))# <class 'int'>
print(type(b))# <class 'bool'>
print(type(c))# <class 'str'>
print(type(d))# <class 'NoneType'>


#By default python provides build in datatypes:

#1. Numeric datatypes:
# int: 3,-8,0
# float: 3.211,-9.0808,0.000001
# complex: 6+2i


# 2.Text datatypes:
# str:"Hello world!!!", "Pyhon programming"

# 3. Boolean datatypes:
# Consist only two values True or false.

# 4.Sequenced datatypes:
# list,tuple

# list: Ordered collection of data with elements separated by a comma and enclosed within square brackets.
#lists are mutable and can be changed or modified after creation.
list1=[8,2.431,[4,9.043],['apple','banana']]
print([list1])

# Tuples are ordered collection of data with elements separated by commas and enclosed by parenthysis
#Tuples are immutable and can not be changed after creation.
tuple1=(("parrot","sparrow"),("Lion","Tiger"))
print(tuple1)

# 5. Mapped datatypes;
# dictnary is the unordered list of data containing a key.

dict1={"name":"Sourav","age":23,"canVote":True}
print(dict1)