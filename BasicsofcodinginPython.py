print("Hello World")
age = 20
price = 19.95
first_name = "Avnish"
is_online = False
print(age)

name = "John Smith"
Age = "20 years old"
Patient = "New"

Name = input("What is your name? ")
print("Hello " + Name)

birth_year = int(input("Enter your birth year: "))
AGE = 2023 - birth_year
print(AGE)

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

# Operator precedence
print(10 + 3 * 2)
print((10 + 3) * 2)

#Conditional Op
y = 3 > 2
print(y)
y = 3 <2
print(y)

#Logical Op
price = 5
print(not price > 10)
print( price>2 and price<7 )
print(price>20 or price<13)

# Strings
print()

course = "Python for Beginners"
#         01234567890123456789
print(course.upper())
print(course)
print(course.find("y"))
print(course.find("for"))
print(course.replace("for", "4"))
print("Python" in course)

# If Statements
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
print()

#Weight Converter Program

print("Weight Converter Program")

weight =int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
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

#Lists

names = ["John", "Bob", "Mosh", "Sam", "Mary"]
#         0       1        2     3       4
#         -5     -4        -3    -2      -1
print(names)
print(names[0])
print(names[-2])
print(names[0:3])  # 0,1 and 2
print(len(names))

#Lists methods

numbers = [1,2,3,4,5]
print(numbers)
numbers.insert(0, -1) # (index, object to be inserted at that index)
print(numbers)
numbers.remove(3)
print(numbers)
numbers.clear()
print(numbers)

numbers = [1,2,3,4,5]
print(2 in numbers)
print(7 in numbers)
print(len(numbers))

print()
# For loops
numbers = [1,2,3,4,5]
for item in numbers:
    print(item)

print()

j=0
while j< len(numbers):
    print(numbers[j])
    j = j + 1

# Range function

numbers = range(5) # range is assumed[0,5)
print(numbers)
for num in numbers:
    print(num)
print()
numbers = range(5,10) # it means [5,10)
for num in numbers:
    print(num)
print()
numbers = range(5, 10, 2) # 2 acts as a step
for num in numbers:
    print(num)

print()

Numbers = (1,2,3,3,4,5,5,2,1,1,7)
print(Numbers.count(1))
print(Numbers.count(5))
print(Numbers.index(2))

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









































