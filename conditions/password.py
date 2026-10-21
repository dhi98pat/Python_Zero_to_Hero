# import random
# import string

# def generate_password(length=8):
#     if length < 4:
#         raise ValueError("Password length must be at least 4")

#     # Ensure password standards
#     uppercase = random.choice(string.ascii_uppercase)
#     lowercase = random.choice(string.ascii_lowercase)
#     digit = random.choice(string.digits)
#     special = random.choice("!@#$%^&*()-_=+")

#     # Remaining characters
#     remaining = length - 4
#     all_chars = (
#         string.ascii_letters +
#         string.digits +
#         "!@#$%^&*()-_=+"
#     )

#     password = [uppercase, lowercase, digit, special]

#     for _ in range(remaining):
#         password.append(random.choice(all_chars))

#     # Shuffle the password
#     random.shuffle(password)

#     return "".join(password)

# # Generate password
# password = generate_password(8)
# print("Generated Password:", password)


###########################################################


import secrets
import string

def generate_secure_password(length=16):
    upper = secrets.choice(string.ascii_uppercase)
    lower = secrets.choice(string.ascii_lowercase)
    digit = secrets.choice(string.digits)
    special = secrets.choice("!@#$%^&*()-_=+")

    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"

    password = [upper, lower, digit, special]

    password.extend(
        secrets.choice(all_chars)
        for _ in range(length - 4)
    )

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

print("Secure Password:", generate_secure_password())