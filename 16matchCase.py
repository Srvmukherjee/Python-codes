#  ITS LIKE SWITCH CASES IN C++, JAVA

x = 4
match x:
    case 0:
        print("x is zero")
    case 4 if x % 2 == 0 and x < 10:
        print(x)
    case _:
        print("x is not zero and not 4 or x is not even and less than 10")


#print the value between 4 to 9

for k in range(4,9):
    print(k)