#ASSIGNMENT – 1
#Name: Lakshmi Prasad
#USN: 25BTLAD001
#Branch: AIDE-B
#DATE: 20-08-26
#UNIT-1
#Task 1
#Print your
#•Name
#•Department
#•College
#Each on a separate line.
#CODE:
print("Name: Lakshmi Prasad")
print("Department: AIDE")
print("College: Jain University")



#Task 2
#Print the following pattern.
#  *******
#  *******
#  *******
#CODE:
for i in range(3):
    print("*******")


#Task 3
#Print the following using a single print() statement.
#Python is Easy
#CODE:
print("Python is Easy")


#Task 4
#Print
#1
#12
#123
#1234
#12345
#CODE:
print("1")
print("12")
print("123")
print("1234")
print("12345")


#Task 5
#Use \n to print
#Computer
#Science
#Engineering
#CODE:
print("Computer\nScience\nEngineering")


#Task 6
#Use \t to print
#Name Age City
#CODE:
print("Name\tAge\tCity")


#Task 7
#Write a Python program with a single-line comment explaining the purpose of the program.
#CODE:
# This program prints a simple message on the screen
print("Python is easy")


#Task 8
#Write a Python program using multi-line comments.
#CODE:
"""
This program prints a simple message.
Multi-line comments are written
between triple quotes.
"""
print("Python is easy")


#Task 9
#Write a program that contains
#•Three comments
#•Three print statements
#CODE:
# Print a greeting
print("Hello")
# Print a welcome message
print("Welcome to Python")
# Print a closing line
print("Python is Easy")


#Task 10
#Create a variable called name.
#Store your name and print it.
#CODE:
name = "Lakshmi Prasad"
print(name)


#Task 11
#Store
#10
#20
#30
#in three different variables and print them.
#CODE:
a = 10
b = 20
c = 30
print(a)
print(b)
print(c)


#Task 12
#Create a program that converts the string "100" into an integer and displays its value and data type.
#CODE:
num = int("100")
 
print(num)
print(type(num))


#Task 13
#Convert the integer 25 into a float and display the result and its type.
#CODE:
num = 25
result = float(num)
 
print(result)
print(type(result))


#Task 14
#Accept the user's age using input(), convert it to an integer, and display the age.
#CODE:
age = int(input("Enter your age: "))
print(age)


#Task 15
#Accept two numbers from the user, convert them to integers, and display their sum.
#CODE:
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
 
total = a + b
print(total)


#Task 16
#(Using f-string)
#Accept a student's name, age and CGPA and display:
#My name is Rahul. I am 20 years old and my CGPA is 8.5.
#CODE:
name = input("Enter your name: ")
age = int(input("Enter your age: "))
cgpa = float(input("Enter your CGPA: "))
 
print(f"My name is {name}. I am {age} years old and my CGPA is {cgpa}.")


#Task 17
#Accept temperature in Celsius and convert it into Fahrenheit.
#Formula: F = (C × 9/5) + 32
#Display the result using an f-string with two decimal places.
#CODE:
celsius = float(input("Enter temperature in Celsius: "))
 
fahrenheit = (celsius * 9 / 5) + 32
 
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")


#Task 18
#Accept an integer and determine whether it is even or odd using the % operator.
#Example:
#Enter number: 25
#Output: 25 is Odd
#CODE:
num = int(input("Enter number: "))
 
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
