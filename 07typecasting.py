#Type casting means Conversion of one datatypes into another datatypes
# Type casting are two types
# 1. Explecit typecasting
# 2. Implicit typecasting


# 1. Explecit typecasting: Conversion of one data types into another datatypes.


string = "10"
number = 21
string_number=int(string)
sum = number+string_number
print(sum)

# 2. Implicit typecasting: One datatypes converted to another datatypes by python interpretor itself.
# python convert a smaller datatypes into higher datatypes to prevent data loss.

a = 10
print(type(a))

b=1.2323
print(type(b))

c=a+b
print(c)
print(type(c))