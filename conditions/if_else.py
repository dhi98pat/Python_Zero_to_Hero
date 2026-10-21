

# x = 10
# r = x % 2

# if r== 0:
#     print("Even")
#     if x>5:
#         print("Greater than 5")
#     else:
#         print("Less than or equal to 5")    

# else:
#     print("Odd")   



##################### 

# x = int(input("Enter the number: "))

# if x == 1:
#     print("One")
# elif x == 2:
#     print("Two")
# elif x == 3:
#     print("Three")
# elif x == 4:
#     print("Four")
# else:
#     print("Wrong input")                




############################ FOR_ELSE####################


nums = [11, 13, 21, 18, 33]

for num in nums:
    if num % 5 == 0:
        print(num, "is divisible by 5")
        break
else:
    print("No number in the list is divisible by 5")
