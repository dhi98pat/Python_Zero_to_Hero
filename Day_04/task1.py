import random
## Option 1
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_choice = random.choice(friends)
print(random_choice)

#### Option 2

random_index = random.randint(0,4)
print(friends[random_index])

