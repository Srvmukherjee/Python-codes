#break statement: this statement enables a progam to skip over a part of code. the break statement terminates the very loop it lies within

# for i in range(1,101,1):
#     print(i,end=" ")
#     if(i==50):
#         break
#     else:
#         print("Hello")
#         print("Sourav")

#continue statement: This statement skip the reamining loop statement and caused the next iteration.
    
for i in [2,4,6,8,10]:
    if(i%2!=0):
        continue
    print(i)

