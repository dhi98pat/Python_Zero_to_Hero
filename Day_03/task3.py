## logical Operators !!
# You can combine different conditions using logical operators.
#
# A and B #Both conditions need to be true
# C or D #Only one condition needs to be true
# not E #The condition must be false

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
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us !!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo=input("Do you want to have a photo take? Type Y for yes and N for No ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill} ")
else:
    print("Sorry, you have to grow tailer before you can ride.")
