# capitalize()--> method only turns first character in uppercase remaining characters are as it is.
str = "sourav"
capstr = str.capitalize()
print(capstr)


str1 = "Hello World"
capstr1 = str1.capitalize()
print(capstr1)

#center()--> This method turns string to the center alling to the text.
str2 = "Welcome to console"
print(str2.center(50))

str2 = "Welcome to console"
print(str2.center(50,"."))

#count()-->This method returns the number of times the given values has occured with in the given string.
str = "Abcdracanhsaklsacsaacsa"
countstr = str.count("a")
print(countstr)


#endswith() - the endswith() method check if the string end with a given value return Ture or return false

name = "Hello world!!!"
print (name.endswith("!!!"))
print (name.endswith("%"))