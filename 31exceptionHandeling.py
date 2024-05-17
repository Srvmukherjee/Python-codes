# Exception handeling: For handle exception input.
# Syntax:
# try:
#     # Statement which could generate.
#     # exception
# except:
#     # Solution of generated exception

# ex - 
try:
    num = int(input("Enter a integer:"))
except ValueError:
    print("Number entered is not an integer.")

# Finally clause: It is also used for exception handeling
    
try:
    num = int(input("Enter the integer value:"))
except ValueError:
    print("Enterd number is not an integer")
else:
    print("Value accepted")
finally:
    print("This block is always executed.")