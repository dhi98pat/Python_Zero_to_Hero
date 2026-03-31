## Function with more than 1 input

# def greet_with(name, location):
#     print(f"Hello, {name}!")
#     print(f"How is it like in, {location}")
# greet_with("John", location="India")

# Keyword Arguments
#
# def greet_with(name, location):
#     print(f"Hello, {name}!")
#     print(f"How is it like in, {location}")
# greet_with( location= "India",name= "John",)

##########################
def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_name = combined_names.lower()
    t = lower_name.count("t")
    r = lower_name.count("r")
    u = lower_name.count("u")
    e = lower_name.count("e")
    first_digit = t + r + u + e

    l = lower_name.count("l")
    o = lower_name.count("o")
    v = lower_name.count("v")
    e = lower_name.count("e")
    second_digit = first_digit + l + o + v + e
    score = int(str(first_digit) + str(second_digit))
    print(score)
calculate_love_score("kanye west", "Kim kardashian")
