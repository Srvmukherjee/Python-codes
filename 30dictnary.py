# PYTHON DICTNARY: Ordered collection of data items. Store multiple items in a single variable.
#  separated by commas and enclosed by{}

namelist = {'name':'Sourav','Age':23,'Egigible':True}
print(namelist)

# Acessing the dictnary items:
# 1. Acessing the single dictnary items:

namelist = {'name':'Sourav','Age':23,'Eligible':True}
print(namelist['name'])             #method 1
print(namelist.get('Eligible'))     #method 2


# 2. Acessing multiple items:   We can print all the value by value().
namelist = {'name':'Sourav','Age':23,'Eligible':True}
print(namelist.values())


# 3. Acessing Keys: We can print all the keys in the dictnary using keys() method.
namelist = {'name':'Sourav','Age':23,'Eligible':True}
print(namelist.keys())

# 4. Acessing key values:
namelist = {'name':'Sourav','Age':23,'Eligible':True}
print(namelist.items())

# Dictnary methods: used for manipulation of dictnary items.
# update(): For add dictnary items.

namelist = {'name':'Sourav','Age':23,'Eligible':True}
print(namelist)
namelist.update({'salary':'5CR'})
print(namelist)

# clear()- Remove all the items from dictnary.
namelist = {'name':'Sourav','Age':23,'Eligible':True}
namelist.clear()
print(namelist)

# pop(): This removes the key value pair whose key is passed as the parameter.
namelist = {'name':'Sourav','Age':23,'Eligible':True}
namelist.pop('Age')
print(namelist)

# popitem() Remove the last key value pair.
namelist = {'name':'Sourav','Age':23,'Eligible':True}
namelist.popitem()
print(namelist)

# del : we use del to remove a dictnary.
namelist = {'name':'Sourav','Age':23,'Eligible':True}
del namelist['Age']
print(namelist)

