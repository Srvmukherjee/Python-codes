# Tuples are ordered collection of data items, they store mu;tiple item in a single variable.
# Tuples are separated by commas and enclosed by round brackets()
# Tuple are unchangable. We can't change tuples

tuple1 = (1,2,3,4,5,6,7,8)
tuple2 = ("Red","Green","Blue")
print(tuple1)


# Tuple indexing: start from index[0].
country = ("India","pakistan","Chaina")
print(country[0])


# 1. Positive indexing: mean indexing start from index[0]-->index[1]-->index[2]-->index[∞]
# 2. Negetive indexing: mean indexing start from last index means index[-1]
country = ("India","pakistan","Chaina")
print(country[-1])


# Range of indexing:
# Syntax -> Tuple[start:end:jumpindex]
animals = ["cat","dog","Horse","Rat","Human","Lion","Tiger"]
print(animals[2:])
print(animals[:2])
print(animals[2:5]) # means index[2]-->index[5-1]=index[4]
print(animals[4:2])# reverse indexing not possible
print(animals[2:7:3])# start from index[2]--->index[2+3]=index[5]


# Qs. Print every 3rd consequtive number:
num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(num[0:14:3])

# Manipulating Tuples: Tuples are immutable, i.e we can change tuple as per our requirement
animals = ["cat","dog","Horse","Rat","Human","Lion","Tiger"]
temp = list(animals)
temp.append("Monkey")# Add item
temp.pop(3)          # Remove item
temp[2] = "Finland"
animals = tuple(temp)
print(animals)

# We can convert tuple to list and vice versa

# Tuple Methods:
# tuple.count(element)
Tuple1= (0,1,2,3,4,5,6,7,1,2,3,5)
res = Tuple1.count(3)
print(res)

# index method:
Tuple1= (0,1,2,3,4,5,6,7,1,2,3,5)
res = Tuple1.index(4)
print(res)