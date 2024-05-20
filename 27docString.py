# Docstring: string literals that appears right after definition of function.

def square(n):
    '''Takes a number and return square of it'''# '''This is called docstring'''
    print(n**2)
square(5)


# Example 2:


def add(num1,num2):
    '''Add two number 
    number 1 = num1
    number 2 = num2
    and return the sum of the number.'''
    num3 = num1+num2
    print(num3)
add(5,3)
print(add.__doc__)
add(2,3)
print(add.__doc__)

# Example 3:

def num(n):
    '''This is square of any number'''
    print(n**2) 
num(5)
print(num.__doc__)






