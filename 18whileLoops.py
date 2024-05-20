# # while loops:
# count=5
# while(count>0):
#     print(count)
#     count = count-1


# #Else with while loops:
    
# count =5
# while(count>0):
#     print(count)
#     count = count-1
# else:
#     print("Counter is 0")


# # # Print the number from 0 to 100, by the help of While loop:
# num = 0
# while(num<=100):
#     print(num) 
#     num += 1

# # Print the number from 100 to 0, by the help of While loop:

# num = 100
# while(num>=0):
#     print(num)
#     num -= 1

# print the multipication table of n

# a=int(input("Enter number"))
# for i in range(1,11):
#         print(i*a)
#         i+=1
        

list1={1,2,3,4,5,6,7,8,9,91,100}
for i in list1:
    print(i)

# Seach a nummber x in the tuple.
    
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 89, 0, 100)
a = int(input("Enter number to find: "))

if a in tuple1:
    index = tuple1.index(a)
    print(f"{a} found in the tuple at index {index}")
else:
    print("Not found")
