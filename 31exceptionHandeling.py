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

# Raising custom errors: we can generate custom errors by raise keyword.
if not 2000<salary<50000:
    raise ValueError("not a valid salary")

