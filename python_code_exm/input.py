## Input from user and add two numbers

# x = input ("Enter the first number: ")
# y = input ("Enter the second number: ")
# z = int(x) + int(y)
# print("The sum is:", z)


## 
import sys
x = int(sys.argv[1])
y = int(sys.argv[2])
z = x + y
print("The sum is:", z)