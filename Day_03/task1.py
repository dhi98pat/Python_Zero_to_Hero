## Control Flow with  if/else and conditional operators..

# if condition:
#     do this
# else:
#     do this

# ######################### First Example ###########################################
# print("Welcome to the rollercoaster!!")
# height = int(input("What is your height in cm?"))
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry you cannot ride the rollercoaster!")
# ######################################################################

# Comparator Operators
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to


############Modulo Operator######################

# modulo_number = int(input("What is number?"))
# if modulo_number % 2 == 0:
#     print("This is the even number")
# else:
#     print("This is the odd number")
####################################################

## Nested if statements and elif statements...


# print("Welcome to the rollercoaster!!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?"))
#     if age <= 12:
#         print("You can't ride the rollercoaster!")
#     elif age >= 18:
#         print("You can ride with parents the rollercoaster!")
#     else:
#         print("You can't ride the rollercoaster!")
# else:
#     print("Sorry you cannot ride the rollercoaster!")

#################################################

# weight= 85
# height= 1.85
# bmi= weight/(height*height)
# bmi=float(input("What is you height?"))
# if bmi >= 25:
#     print("overweight")
# elif bmi >= 18.5:
#     print("normal weight")
# else:
#     print("obese")

#########################################################

print("Welcome to the rollercoaster!!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo=input("Do you want to have a photo take? Type Y for yes and N for No ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill} ")
else:
    print("Sorry, you have to grow tailer before you can ride.")


