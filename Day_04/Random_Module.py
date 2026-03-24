## Random Module

##Computers are not random, because they are built with circuits and switches. But randomness is very important when building software, especially games. It would be really boring if every move in a video game was pre-determined.
#################################################################

import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)

# random_choice = random.choice(["Heads", "Tail"])
# print(random_choice)

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")


