## Method 1: Using Python Tuple Unpacking.
a = 10
b = 20

print("Before Swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("\nAfter Swapping:")
print("a =", a)
print("b =", b)


## Method 2: Using Bitwise XOR

a = 10
b = 20

a = a ^ b
b = a ^ b
a = a ^ b

print("a =", a)
print("b =", b)