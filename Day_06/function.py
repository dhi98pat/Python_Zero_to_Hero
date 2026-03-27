############ Function ################
# A function in its simplest form is just a wrapper name for a block of code. You give it name and then when you call the function by that name, all the code within the function block will be executed. It can help us save time and reduce repeated code.
#####################################
# Defining a new Function
# def <function name>():
#def my_function():
    # do this
    # Then do this
    # Finally do this.
## Calling the function
#my_function()

###################################
# print("Hello")
# num_char = len("Hello")
# print(num_char)

# def my_function():
#     print("Hello World")
#     print("Hello World!!!")
# my_function()

######################################


#Creating the function
def get_user_name():
    name = input("What is your name? ")
    print("Hello, " + name)
    # Inside the function

#Outside the function
print("Hello")
get_user_name() # Calling the function