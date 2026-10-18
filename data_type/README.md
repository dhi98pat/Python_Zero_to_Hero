A data type defines the kind of value a variable can store and what operations can be performed on it.

Integer (int)

Stores whole numbers.

Python
age = 25
print(age)
print(type(age))

Output:

Python
25
<class 'int'>
Float (float)

Stores decimal numbers.

Python
price = 99.99
print(price)
print(type(price))

Output:

Python
99.99
<class 'float'>
Complex (complex)

Stores complex numbers.

Python
num = 3 + 4j
print(num)
print(type(num))

Output:

Python
(3+4j)
<class 'complex'>

2. String Data Type (str)

Stores text enclosed in quotes.

Python
name = "Dhiraj"
city = 'Delhi'
 
print(name)
print(type(name))

Output:

Python
Dhiraj
<class 'str'>

Common string operations:

Python
text = "Python"
 
print(text.upper()) # PYTHON
print(text.lower()) # python
print(len(text)) # 6

3. Boolean Data Type (bool)
Stores either True or False.

Python
is_logged_in = True
print(is_logged_in)
print(type(is_logged_in))

Output:

Python
True
<class 'bool'>

Example:

Python
age = 18
print(age >= 18)

Output:

Python
True

4. List Data Type (list)

An ordered, mutable collection of items.

Python
fruits = ["apple", "banana", "mango"]
 
print(fruits)
print(type(fruits))

Output:

Python
['apple', 'banana', 'mango']
<class 'list'>

Modify a list:

Python
fruits.append("orange")
print(fruits)

Output:

Python
['apple', 'banana', 'mango', 'orange']
5. Tuple Data Type (tuple)

Ordered but immutable collection.

Python
coordinates = (10, 20)
 
print(coordinates)
print(type(coordinates))

Output:

Python
(10, 20)
<class 'tuple'>

Attempting to change a tuple raises an error:

Python
coordinates[0] = 15

❌ Error because tuples cannot be modified.

6. Set Data Type (set)

Unordered collection of unique items.

Python
numbers = {1, 2, 3, 4, 4, 5}
 
print(numbers)
print(type(numbers))

Output:

Python
{1, 2, 3, 4, 5}
<class 'set'>

Notice duplicate 4 is automatically removed.

Adding an element:

Python
numbers.add(6)
print(numbers)
7. Dictionary Data Type (dict)

Stores data in key-value pairs.

Python
student = {
"name": "Dhiraj",
"age": 28,
"city": "Noida"
}
 
print(student)
print(type(student))

Output:

Python
{'name': 'Dhiraj', 'age': 28, 'city': 'Noida'}
<class 'dict'>

Access values:

Python
print(student["name"])

Output:

Python
Dhiraj
8. Binary Data Types
Bytes (bytes)
Python
data = b"Hello"
 
print(data)
print(type(data))

Output:

Python
b'Hello'
<class 'bytes'>
Bytearray (bytearray)

Mutable version of bytes.

Python
data = bytearray(5)
print(data)

Output:

Python
bytearray(b'\x00\x00\x00\x00\x00')
Type Conversion

Convert one data type into another.

Python
age = "25"
 
print(type(age))
 
age = int(age)
 
print(type(age))

Output:

Python
<class 'str'>
<class 'int'>

Examples:

Python
int("100") # String to Integer
float("12.5") # String to Float
str(100) # Integer to String
list((1, 2, 3)) # Tuple to List
Quick Summary Table
Data Type	Example	Mutableint	10	No
float	10.5	No
complex	2+3j	No
str	"Python"	No
bool	True	No
list	[1,2,3]	Yes
tuple	(1,2,3)	No
set	{1,2,3}	Yes
dict	{"name":"Dhiraj"}	Yes
bytes	b"abc"	No
bytearray	bytearray(5)	Yes