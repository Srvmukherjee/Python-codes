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


#We can also check for a value between the string by providing start and end index position.
str1 = "Welcome to the console"
print(str1.endswith("to",4,10))

#find()- Seaches for the first occurance of the value and return the index, if not find then return -1.
str4 = "My name is Sourav Mukherjee "
print(str4.find("is"))
print(str4.find("Bhaskar"))

#index()- Searches for the first occurance and return the index value. If not present then raise exception.
str5 = "My name is Sourav Mukherjee, I pursuing Btech from Heritage Institute of Technology, Kolkata."
print(str5.index("Heritage"))
#print(str5.index("Electronics"))

#isalnum()- This method returns True if the entire message contains "A-->Z", "a-->z","0-->9" return True, if any another types of string present return False
str6 = "My name is Sourav Mukherjee I am 23 years old"
print(str6.isalnum())
str7 = "WelcomeToTheConsole"
print(str7.isalnum())

#isalpha()- This return true is only there is contains only A->Z, a->z if any character or number 0->9 present in the string return False.
str1 = "Weclome"
print(str1.isalpha())
str2 = "Welcome27"
print(str2.isalpha())
str3 = "Welcome Sourav"
print(str2.isalpha())

#islower()-->Return true if and only if there are all small letter present in the string. If not return false.
str1= "hello world"
print(str1.islower())

#isprintable()-> If the given string are printable. if not return false.
str1= "Sourav is a electronics and Communication engineer."
print(str1.isprintable())

#isspace()--> return true if the string only contains space. Else it return false.
str=" "
print(str.isspace())
str1 = "Hello world"
print(str1.isspace())

#startswith()--> the startswith() return true if the string first word starts with given value. If not return false.
str= "Python is a programming language."
print(str.startswith("Python"))
print(str.startswith("python"))

#swapcase()--> Convert the uppercase into lower case and vice versa.
str="Hellow world"
print(str.swapcase())

#title()- capitalizes each letter of word within the string.
str = "He is an engineer"
print(str.title())

