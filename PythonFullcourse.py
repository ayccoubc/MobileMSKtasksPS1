# First Python Program
print("Hello World")
age = 20
price = 19.95
first_name = "Avnish"
is_online = False
print(age)

name = "John Smith"
Age = "20 years old"
Is_new = True

Name = input("What is your name? ")
print("Hello " + Name)   # String Concatenation

birth_year = int(input("Enter your birth year: "))   # Type conversion.
AGE = 2023 - birth_year
print(AGE)
print("You are " + str(AGE) + " years old")

color = input("What is your favourite color? ")
print(Name + "likes " + color + "color.")

print("*" * 10)
print()

# Arithmetic Operators

print()

print(3+10)
print(3-10)
print(3*10)
print(3/10)
print(3//10)
print(3**10)
print(3%10)

x = 10
print(x)
x -= 3
print(x)
x += 3
print(x)
x *= 3
print(x)
x /= 3
print(x)

# Operator precedence  EBODMAS. E - exponential.
print(10 + 3 * 2)
print((10 + 3) * 2)

# Math Functions
import math
z = 2.8
print(round(z))   # Rounding off
print(abs(-2.8))  # Absolute value.
print(math.ceil(2.8))
print(math.floor(2.8))   # Google python 3 math module.

# Conditional Op
y = 3 > 2
print(y)
y = 3 <2
print(y)

# Logical Operators
# and - both conditions be true
# or - at least one be true
# not - inverts the output.

price = 5
print(not price > 10)
print(price > 2 and price < 7)
print(price > 20 or price < 13)
print()

# Strings

print()

course = "Python for Beginners"
#         0123456789....   indices of characters
print(course[3])
print(course[-3])
print(course[2:5]) # prints char with indices from 2 to 4. [2,5)
print(course[0:])  # all char printed
print(course[:])   # all char printed
print(course[1:]) # first char excluded
print(course[:5]) # same as [0:5]
print(course[1:-1])
print(course.upper())
print(course)
print(course.find("y"))   # string method, it is case sensitive.
print(course.find("for"))
print(course.replace("for", "4"))
print("Python" in course)
print(len(course))

Course = "Python's Course"
cOurse = 'Python for "Beginners".'
coUrse = ''' Python's Course for "Beginners". '''

first = "John"
last = "Smith"
message = first + " [" + last + "] is a coder. "
print(message)
msg = f"{first} [{last}] is a coder. "  # formatted string
print(msg)


# If Statements
# Comparison Operators - >, <, >=, <=, ==, !=. O/p is True or False.
print()
temp=35
if temp>30:
    print("It's a hot day")
    print("Drink water")
elif temp>20: # (20,30]
    print("It's a nice day")
elif temp>10: # (10,20]
    print("Its a bit cold")
else:
    print("Its cold.")
print("Done.")

is_hot = True     # Executed
is_cold = False    # Not executed

if is_hot:
    print("It's a hot day. ")
    print("Drink Plenty of water")
elif is_cold:
    print("Its a cold day. ")
    print("Wear warm clothes. ")
else:
    print("Its a lovely day. ")
print("Enjoy your day. ")

Price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * Price
else:
    down_payment = 0.2 * Price
print(f"Down Payment: ${down_payment}")

NAME = input("Enter your name: ")

if len(NAME) < 3:
    print("Name must be at least 3 charcters long.")
elif len(NAME) > 50:
    print("Name must be a max of 50 char. ")
else:
    print("Okie Dokie.")

print()

# Weight Converter Program

print("Weight Converter Program")

weight =int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":   # Converts input string to all uppercase.
    converted = weight/0.45
    print("Weight in lbs: " + str(converted))
else:
    converted = weight*0.45
    print("Weight in Kgs: " + str(converted))


print()

# Loops, Lists, Range, tuples

print()

i=1
while i<=5:
    print(i)
    i=i+1

i=1
while i<=5:
    print(i* "#")
    i=i+1
print("DoNE")
print()

# Lists

names = ["John", "Bob", "Mosh", "Sam", "Mary"]
#         0       1        2     3       4
#         -5     -4        -3    -2      -1
print(names)
print(names[0])
print(names[-2])
print(names[0:3])  # 0,1 and 2
print(names[2:4])  # 2 and 3
print(len(names))
names[2] = "Josh" # Replacing
print(names)
# Just like strings.

NUMbers = [3, 6, 2, 10, 4, 8]
max = NUMbers[0]
for number in NUMbers:
    if number > max:
        max = number
print(max)

# 2D Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
print(matrix[1][2])

for row in matrix:
    for item in row:
        print(item)

matrix[2][2] = 12
print(matrix)

# Lists methods

numbers = [1,2,3,4,5]
print(numbers)
numbers2 = numbers.copy()
print(numbers2)
numbers.append(10)
print(numbers)
print(numbers2)
numbers.insert(0, -1) # (index, object to be inserted at that index)
print(numbers)
numbers.remove(3)
print(numbers)
numbers.pop()
print(numbers)
numbers.clear()
print(numbers)

numbers = [1,2,3,4,5,5,6,6,6]
print(2 in numbers)
print(7 in numbers)

print(numbers.count(5))
print(len(numbers))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

print()
# For loops
numbers = [1,2,3,4,5]
for item in numbers:
    print(item)
# item will be equal to 1 element of list in each loop from left to right.

j=0
while j< len(numbers):
    print(numbers[j])
    j = j + 1
print("Done.")


Color = "Blue"
for item in Color:
    print(item)
# item will be equal to 1 char in each loop from left to right. item acts as a variable.

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total price is ${total}")

print()

# Nested Loops
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

Numbers = [5, 2, 5, 2, 2]
for x_count in Numbers:
    output = ""
    for count in range(x_count):
        output += "x"
        print(output)
# OR
Numbers = [5, 2, 5, 2, 2]
for x_count in Numbers:
    print("x" * x_count)


# Range function

numbers = range(5)  # range is assumed[0,5)
print(numbers)
for num in numbers:
    print(num)
print()
numbers = range(5,10)  # it means [5,10)
for num in numbers:
    print(num)
print()
numbers = range(5, 10, 2)  # 2 acts as a step
for num in numbers:
    print(num)

print()

# Tuples

Numbers = (1,2,3,3,4,5,5,2,1,1,7)
print(Numbers.count(1))
print(Numbers.count(5))
print(Numbers.index(2))

print()
# Unpacking
coordinates = (1, 2, 3)

x, y, z = coordinates  # Same as x = coordinates[0], y = coordinates[1], z = coordinates[2]
# This is unpacking.
print(x)
print(y)
print(z)


print()
#Basic Calculator
print("BASIC CALCULATOR")
First = float(input("First Number: "))
Second = float(input("Second Number: "))

Sum = First + Second
Difference = First - Second
Product = First*Second
Division = First/Second

print("Sum is " + str(Sum))
print("Difference is " + str(Difference))
print("Product is " + str(Product))
print("Division is " + str(Division))
print()

# Guessing Game

correct_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess:'))
    guess_count += 1
    if guess == correct_number:
        print('you won!')
        break
else: print("Sorry, no more guesses left. ")

# Car Game
command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped...")
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car 
quit - to quit
        ''')
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand what you are saying. ")


# Program to remove duplicates in a list

NUMBERS = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for nom in NUMBERS:
    if nom not in uniques:
    uniques.append(nom)
print(uniques)
print()

# Dictionary
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
print(customer.get("name"))
print(customer.get("Name"))

customer["birthdate"] = "Jan 1 1980"
# Adding more data in dictionary
print(customer["birthdate"])

Phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
}
output= ""
for ch in Phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

# Emoji Converter
message = input(">")
words = message.split(' ')
emojis = {
    ":)" : "smily face",
    ":(" : "sad face"
}
for word in words:
    output += emojis.get(word, word) + " "
print(output)

# Functions

def greet_user():
    print("Hi There!")
    print("Welcome Aboard")


print("Start")
greet_user()
print("Finish")

# Parameters
def greet_user(name):
    print(f"Hi There! {name}")
    print("Welcome Aboard")

print("Start")
greet_user("John")
greet_user("Mary")
print("Finish")

def greet_user(first, last):
    print(f"Hi There! {first} {last} !")
    print("Welcome Aboard")


print("Start")
greet_user("Avnish", "Bro")  # Positional Arguments - order matters
print("Finish")

print("Start")
greet_user(last = "Arvin", fisrt =  "Murphy") # Keyword Arguments - order doesnt matter
greet_user("mary", first = "Bloody")   # Keyword be used after Positional
print("Finish")
print()

# Return Statement

def square(n):
    n*n
    return n*n  # Gives the output to the original lines of code.


print(square(3))

# Creating a reusable functions:
# Function should not contain input or output code.
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "smily face",
        ":(": "sad face"
    }
    for word in words:
        output += emojis.get(word, word) + " "
        return output


message = input(">")
print(emoji_converter(message))

# Handling Errors , using try and except.
# Preventing crashes.

try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:    # Possible Errors.
    print("Age Can't be zero.")
except ValueError:
    print("Invalid value")

# Class

class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()  # 1 Object
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()  # 2nd Object
point2.x = 15
print(point2.x)

# Constructors
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
print(point.x)

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()

# Inheritance

class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    pass

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()

# Modules
# Files with code.

import converters

print(converters.lbs_to_kg(70))

# OR

from converters import kg_to_lbs

print(kg_to_lbs())

# Finding max number

from utils import find_max

numbers = [10, 3, 6, 2]
maximum = find_max(numbers)
print(maximum)

# Package

import ecommerce.shipping

ecommerce.shipping.calc_shipping()

# OR

from ecommerce.shipping import calc_shipping

calc_shipping()

# Generating Random values

import random

for i in range(3):
    print(random.random())

members = ["John", "Mary", "Mosh", "Bob"]
leader = random.choice(members)
print(leader)

# Rolling Dice
import random

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randit(1,6)
        return first, second


dice = Dice()
print(dice.roll())

# Files and Directories

from pathlib import Path

Path("ecommerce")
print(path.exists())

path = Path("emails")
print(path.mkdir())

path = Path()
for file in path.glob('*.py'):
    print(file)

# pypi.org ---- useful website.
































