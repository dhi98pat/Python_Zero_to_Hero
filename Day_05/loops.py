### For Loop
# Loop allow us to tell the computer to repeat actions without having to write repeated code. If we wanted the computer to print out 1 through to 100, it would very painful to type a print statement for every number, or even just typing out all the numbers 1 through to 100. Loops allow us to create a rule and the computer can follow it to do a repeated action.
#########################################
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
# print(fruits)
#############################################

# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# total_scores = sum(student_scores)
# #print(total_scores)
# sum = 0
# for score in student_scores:
#     sum += score
# print(sum)
# print(total_scores)
##############################################

# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score
# print(max_score)

#########################################################

# exam_mark = [8,65,89,86,55,91,64,89]
# max_mark = 0
# for mark in exam_mark:
#     if mark > max_mark:
#         max_mark = mark
# print(max_mark)

##########################################################

## for Loop for Range function..
# range (1,10)
# range_item = range (1,10)
# print(range_item)

###################################################
#
# range (1,100)
# range_item = range (1,100)
# sum (range_item)
# print(sum (range_item))


###########################################
#
# total = 0
# for num in range(1,101):
#     total += num
# print(total)
#
###########################################

## Create a loop with For and Range to go from 1 to 100.
for number in range(1,101):
    # First check if the number is divisible by both 3 and 5.
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # Then chck if the number is only divisible by 3
    elif number % 3 == 0:
        print("Fizz")
    # Finally check if the number is only divisible by 5
    elif number % 5 == 0:
        print("Buzz")
    # If it's not divisible by either of those numbers, just print the number
    else:
        print(number)




