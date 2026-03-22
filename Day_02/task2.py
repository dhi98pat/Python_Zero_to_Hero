## Type Error, Checking and Conversion

#TypeError
#These errors occur when you are using the wrong data type. e.g. len(12345)
#Because you can only give the len() function Strings, it will refuse to work and give you a TypeError if you give it a number (Integer).
#PAUSE 1. Fix the len() function so it has no more warnings or errors.
# print(type("abc"))
# print(type(1234))
# print(type(123.45))
# print(type(True))
# print(type(False))
#
# # Type Conversion
# str()
# int()
# float()
# bool()
#
#print(int("123") + int("456"))
name_of_the_user = input("Enter your Name")
length_of_the_name = len(name_of_the_user)

print(type("Number of letters in your name: "  )) # str
print(type(name_of_the_user)) # init

print("Number of letters in your name: " + str(length_of_the_name))