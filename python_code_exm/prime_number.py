# num = 10

# for i in range(2, num):
#     if (num % i) == 0:
#         print(num, "is not a prime number")
#         break
# else:
#     print(num, "is a prime number")


### Function Version of prime number.
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True
print(is_prime(29))
print(is_prime(30))



