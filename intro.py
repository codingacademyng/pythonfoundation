# INTRODUCTION TO PYTHON
# Python is the most popular programming language, it is rated the most used by Popularity of Programming language (index) index
"""
Python is an object-oriented scripting language that was released publicly in 1991. It was
developed by Guido van Rossum of the National Research Institute for Mathematics and
Computer Science in Amsterdam.
Python has rapidly become one of the world’s most popular programming languages.
It’s now particularly popular for educational and scientific computing, and it recently
surpassed the programming language R as the most popular data-science programming
language. Here are some reasons why Python is popular and everyone should consider
learning it:
• It’s open source, free and widely available with a massive open-source community.
• It’s easier to learn than languages like C, C++, C# and Java, enabling novices and
professional developers to get up to speed quickly. 
"""

'''
This is a comment'''






# print("Today is Friday")  



# comments

# python has commenting capability for the purpose of in-code documentation
# comments start with a hash, and python will render the rest of the line as a comment

#  print("Hello World")

# why do we comment
# comments are used to explain python code or for documentation
# e.g
# this is to print a message on the screen
# print("Welcome to python class. it promises to be exciting.") # this is to print a message on the screen
# this is to print a message on the screan

# comments can be used to prevent execution when testing code

# "fiath"
# junaid
# sade
# cosmoss
# sheriff

# Multiline comment

"""
today is monday
I'm gonna learn python
"""

"""
this is the first class of python
we are good to go for robotic class
this program runs for couple of months
and we will surely succeed in it
"""

# Variables Declaration
# variables are containers for storing data value, a variable is created the moment you assign a value to it

# myName = "Maranatha"
# variableName = "This can be anything"

# print(myName)
# print(variableName)

std_name = "TIMI"
location = "Ogbomoso"
state = "Oyo"

# print('my name is TIMI and i am from Ogbomoso in oyo State')
# print("my name is " + std_name + " and I am from " + location + " in " + state + " state")
# print(f"my name is {std_name} and I am from {location} in {state} state")

# print("my name is " + std_name + " and i am from" + location + "in " + state + "state") #"+" this means "concatenation sign", it is used to joined strings together
# print(f"My name is {std_name} and i am from {location} in {state} state") #"f" is used as formated string, it is always needed in the case of formating of strings.

# location = "Ibadan"
# state = "Lagos"
# print(f"I am {std_name} and i am located in {location} in {state} state")

# Variable name
# A variable name must start with a letter or the underscore character

name = "ade"
_name = "ade"
# print(Name)
Name = "bayo"
# print(_name)
# x = 'ADE'
# print(x)
# _x = "tunde"
# print(_x)

# A variable name cannot start with a number

# 12_student = "ade"
# print(12_student)

# A variable name can only contain alpha-numeric characters and underscores
# ade_123 = "Male"
# tunde123 = "MALE"
# print(tunde123)
# print(ade_123)

# variable names are case-sensitive
#  tolu, Tolu, TOLU
# name = "ade"
# print(name)
student = "tolu"
# print(Student)
# tolu = 10
# print(tolu)

# python keywords cannot be used as a variable name
# is = "Jss1"
# print(is)

# Multi words variable names
# Camel case
# e.g
mySecondName = "Shola"

# myFirstName = "something"


# js1StudentName = "Bayo"


# print(studentName)
# snake case - each words separated by an underscore
# # e.g
# student_name_one = "Ade"
# print(student_name_one)

# ways of declaring a variable
fname = "ade"
lname = "Toba"
location = "ogbomosho"
state = "Oyo"

# Assigning Multiple values

fName, lName, location, state = "Yemi", "Sunday", "Ogbomoso", "Oyo state"
# print(fName)
# print(location)
# total = [fName, lName, location, state]
# print(total)
# print(fName)
# print(location)
# print(state)

# one value to multiple variable
# x = "pawpaw"
# y = "pawpaw"
# z = "pawpaw"
# x = y = z = "pawpaw"
# print(x)
# print(y)
# print(z)
# sqi = rein = dataforme = 'Dugbe', 'Iwo Road', 'Mokola'
# fName, lName, location, state = "Yemi", "Sunday", "Ogbomoso", "Oyo state"
# print(sqi)
# print(rein)
# print(dataforme)


# unpacking a collection - if you have a collection of values in a list, python allows you to extract the values into varaiables
# fruits = ["apple", "pawpaw", "orange"]
w, x, y, z = ["apple", "pawpaw", "orange", "Gauva"]
# print(w)
# print(x)
# print(y)
# print(z)

# myName = input("Enter your name ")
# print(myName)

# date = input("What is today's date? ")
# print(date)

# username = input("Enter your name ")
# print(f"Your username is {username}")

# name = input("supply your name ")
# location = input("supply your location ")
# print('Hello ' + name + ' you are from ' + location)

# Concatenation sign plus +
name = 'ade'
location = "Ibadan"
age = 14
# print("my name is " + name + " i live in " + location + " my age is " + str(age))
# print(f"my name is {name} i live in {location} my age is {age}")


# fName, lName, location, state = "Yemi", "Sunday", "Ogbomoso", "Oyo state"
# fName = "Ade"
# lName = "sunday"
# state = "oyo state"
# location = "General area"
# score = 70
# score1 = str(score)
score1 = "70"
# print("My name is " + fName +  lName + "  I Stay at " + location +  state + " and my total score is " + score1)
# print("My name is " + fName + " " + lName + "  I Stay at " + location + " " +  state + " and my total score is " + score1)


# use of input() - to collect information from user
# name = input("please supply your name ")
# food = input("supply the food you would like to buy ")
# Quantity = input("supply the plates of food you want to buy ")
# print("my name is " + name + " i will like to order for " + Quantity + " plates of " + food)

# val1 = int(input('Enter your first value: '))
# val2 = int(input('Enter your second value: '))

# val1 = "10"
# val2 = "20"
# print(val1 + val2)


# total = val1 + val2
# print(total)


#Assignment: Write a python program that would users to supply their firstname, lastname, age, address, first value and second value. Output a message saying: Hello user's firstname, lastname, your age is user's age and you are from user's address. The result of your operation is (subtraction of value1 from value2)



# # Global and Local variables - variables are created outside of a function
#  function is a named section of a code that performs a specific task

# def sewa():
#     name = 'sewa'
#     location = "ibadan"
#     print(name, location)


student_name = "tunde" #global variable
# print(student_name)
# def name():
#     print(student_name)
# name()
# def name():
#     student_name = "ade" #local variable
#     print(student_name)
# name()
# print(student_name)
# a = 10
# a = 15
# print(a)
# def std():
#     student_name = "ade"
#     print(student_name)
# std()


# x = "Tolu"
# def name():
#     y = "Ade"
#     print(y)
#     print(x)
# name()


# Global variable can be used by everyone, both inside and outside of function
# Local variables are variables that are declared inside a function and can only work inside the function they are been declared
a = 20  #global variable
b = 0

# def subtract():
#     # global a
#     a = 10
#     score = a - b
#     print("Subtraction is ",score)
# subtract()
# # print(a)
# def addition():
#     # global b
#     b = 10   #local variable
#     score = a + b
#     print("Addition is ",score)


# # subtract()
# addition()


# Assignment
# Write a program that will ask a user the following information;
# firstName, lastName, location, value1, value2, then you are going to perform addition operation on the values the user supplies as value1 and value2 together
# then print a statement having all the information the user supplied
# i.e my full name is......, i am from ......, my total score is.....

# DATA TYPE
# Datatypes
# Datatypes are the classification or categorization of data items.
# It represents the kind of value that tells what operations can be performed on a particular data
# since everything is an object in python, data types are actually classes and variables are instance
# (object) of these classes.

# name = "tola"
# print(type(name))

# val1 = 10
# print(type(val1))

# name = "10"
# print(type(name))

# val2 = 10.2
# print(type(val2))


# myNames = ["Ade", "Bade", "Tola", "Fola"]
# print(type(myNames))

# myOtherNames = ("Bola", "Dayo", "Femi")
# print(type(myOtherNames))


# decision = True
# decision2 = False
# print(type(decision))

# name = ["ojo", 10, True]
# name1 = ("ojo", 10, True)
# name2 = range(10, 45)
# print(type(name2))

# #Creating a new paragraph

# print("Today is Tuesday.\nI'm currently in class learning python.\nI'm gonna try my best")

# print("""
# Today is thursday
# I want to learn a new thing
# I will practice at home also      
# """)

# Types of Datatype
# 1. Text types: String (str) a string is collection of one or more characters put in a quote
# 2. Numeric types- represent the data which has numeric value: integer(int), float, complex
# 3. Sequence types - ordered collection of different data types. it allows multipe values to be stored: list, tuple, range
# 4. Mapping types: dictionary(dict)
# 5. Set types - is an unordered collection of data type that is iterable, mutable and has no duplicate element: set, frozenset
# 6. Boolean types - data type with one of the two built-in values, True or False: bool (True, False)
# 7. Binary types: bytes, bytearray, memoryview

# Examples
# string (str)  #example: "Johnson", "False", "56", 'b' '5.9', "this is my first python class"
# integer (int) example: 65, 80, 1, 254854
# float (float) example: 7.8, 5.5, 0.3
# complex example: 10j


# list example:
# mm =  list((1,  3, 4, "one", "two", True, False, 10j, 10.1))
# mm =  [1,  3, 4, "one", "two", True, False, 10j, 10.1]
# print(type(mm))
# numbering = """
# 1. Faith 
# 2. Sola
# 3. Ola
# """

# print(type(numbering))

# tuple example: (5, 55, 7), tuple((5, 55, 7)) title()
# range example: range(10)

# dictionary example: {"school":"SQI", "course":"Python"}, dict((name="Ola", age=22))
# stds = {"Ade":"Ajayi"}
# print(type(stds))
# x = 5.0
# print(type(x))

# student = "name"
# print(type(student))

# student_name = {"tunde":10, "ade":20, "femi":30}
# print(type(student_name))

# set example: {1,2,3,4,5,6}
# mm = ({1,2,3,4,5,6})
# print(type(mm))
# frozenset example: ({1,2,3,4,5,6})
# bool example: True, False
# bytes example: b"Hello"


# Datatypes conversion - casting

# str()
# float()
# int()
# list()
# tuple()
# dict()
# set()



val = 10
# newVal = str(val)
# print(type(newVal))

# val2 = "10"
# newVal2 = int(val2)
# print(type(newVal2))

# print("My total result is " + str(val))


# score1 = int(input("ENter your first score "))
# score2 = int(input("ENter your second score "))

# result = score1 + score2
# print(result)

# result = int(score1) + int(score2)
# print(result)

# print("The result of your operation is " + str(result))

# To check for datatypes use type() function

# print(type(score1))

# val = 10.9
# fl_val = int(val)
# print(fl_val)

# score = "30"

# score1 = int(score)
# score2 = 20
# total = score1 + str(score2)
# print(total)
# print(type(total))
# print(score1)
# print(type(score1))
# score2 = int(score)
# score1 = str(7.5)
# print(score1)
# print(type(score1))
# print(type(score2))

# name = "Yemi"
score = 7
# score1 = int(name)
# print(score1)

# num1 = 20
# num2 = float(num1)
# print(num2)

# print(type(name))
# # str() to convert to string type
# print("Type before convertion ", type(score))
# print("Type after convertion ", type(str(score)))
# # int() to convert to integer type
# print("Type before convertion ", type(score))
# print("Type after convertion ", type(int(score)))
# print("Actual value after convertion ", int(score))
# print("Not all value can be converted to integer ",int(score))
# # float() to convert to float
# print("Type before convertion ", type(score))
# print("Type after convertion ", type(float(score)))
# print("Actual value after convertion ", float(score))
# # bytes() to convert to bytes
# print("Type before convertion ", type(name))
# print("Type after convertion ", bytes(name, 'utf'))

# list() to convert to a list object
# my_name = ("Yemi", "Tope", "Sunday")
# name = list(my_name)
# print(list(my_name))
# print(my_name)
# print(type(name))
# print("Type before convertion ", type(my_name))
# print("Type after convertion ", type(list(my_name)))
# my_name = ("Yemi", "Tope", "Sunday")
# name = set(my_name)
# print(type(my_name))
# print(type(name))
# print(name)
# set() to convert to a set object
# tuple() to convert to a tuple object
# dict() to convert to a dictionary object


# Example
# value1 = input("enter first number ")
# value2 = input("enter second number ")
# result = int(value1) + float(value2)
# print("The total result is " + str(result))
# print(f"The total result is {result}")

# operators
# they are special symbols that designate the sort of computation to be performed.
# Types of Operator
# 1. Arithmetic operators - operators that performs mathematic operation: +, -, /, *, %, //, **

# print(9 // 2)

# 2. Assignment operators- assigns values to the operands on the left hand side: =, +=, -=, /=, *=, //=, %=, **=,  etc

# val = 30
# print(val + 5)
# val += 5
# print(val)
# val -= 5
# val /= 5

# user_score = 40
# print(user_score)
# exam_score = int(input("Enter your exam score "))
# user_score += exam_score
# print(user_score)

# newval = 40
# newval //= 10
# print(newval)

# 3. Comparison operators- to compare numbers or strings and returns boolean ==, !=, >, <, <=, >=,

# val = 9
# val2 = 8
# print(val == val2)
# print(val <= val2)
# print(val != val2)


# 4. Logical operators - to combine conditional statement : and, or, not
# 5. Identity operators: to compare objects, not if they are equal but if they are actually the same object: is, is not

# val1 = 20
# val3 = 40
# print(val1 is val3)

# 6. Membership Operators - to test if a sequence is present in an object: in, not in

# arr1 = ["Ade", "Bola", 20, 30]
# print("ade" in arr1)

# 7. Bitwise operators - used to perform bitwise operations on bit patterns or binary numerals: &, |, ^, ~, <<, >>

# x = 20
# x + 5
# x += 5
# print(x)
# x += 5
# print(x)
# Arithmetic Operators
# fval = 7
# sval = 2

# total = fval + sval
# print(total)
# print(fval ** sval)
# print('The addition of the two variables is ' + str(total))
# print('for subtraction '+ str(fval - sval))
# print('for multiplication '+str(fval * sval))
# print('for division '+str(fval / sval))
# print('for modulus '+str(fval % sval))
# print('for exponentiation '+str(fval ** 2))
# print('for floor division '+str(fval // sval))

# assignment Operators
# fval = 30
# sval = 10
# fval += 5          #(fval = fval + 5)
# print(fval)
# fval -= 5
# print(fval)
# fval /= 5
# print(fval)
# fval *= 5
# print(fval)
# fval %= 7
# print(fval)
# fval //= 7
# print(fval)
# fval **= 4
# print(fval)

# #Comparison Operators
fval = 8
sval = 10
# print(fval == sval)
# print(fval != sval)
# print(fval > sval)
# print(fval < sval)
# print(fval >= sval)
# print(fval <= sval)

# #Logical Operators
# A      B       A and B       A or B       not A

# T      T          T            T           F

# T      F          F            T           F

# F      T          F            T           T

# F      F          F            F           T

fval = 10
sval = 5
# print(fval == sval and fval >= sval)
# print(fval != sval or fval >= sval)
# print(not(fval >= sval))
# print((fval == sval or fval >= sval) and (fval > sval and fval >=sval))

# day1 = "wednesday"
# day2 = "not christmas"
# time = "1am"
# weather = "dark"
# if (day1 == "wednesday" and day2 == "not christmas") and time == "1am" and weather == "dark":
#    print('I will come to SQI')
# else:
#     print("I will stay at home")

# Identity Operators
# fval = 10
# sval = 5
# print(fval is sval)
# print(fval is not sval)

# Membership Operator
# fval = ["sola", "tunde", "monday", "sunday"]
# print("sola" in fval)
# print("sola" not in fval)
comment = "this is a python class for iot and robotics"
# print('class' in comment)
# print("python" not in comment)

# #Bitwise Operators
fval = 45
sval = 36

# 45 | 2 - 101101
# 22 | 2
# 11 | 2
# 5 | 2
# 2 | 2
# 1 | 2

# print(bin(fval))   #101101
# print(bin(sval))   #100100

# print(bin(fval & sval)) # = 100100 this confirms that the two parameters must be positive
# print(bin(sval | fval)) # = 101101 this confrims that any of the conditions myst be postive
# print(bin(sval ^ fval)) # = 001001 this returns 0 whereever the two values are the same
# print(bin(~ fval)) # = 010010 this returns the oppostie of the values
# print(bin(sval << 2)) #this adds two zeros to the end of the values
# print(bin(sval >> 2)) #this shift it to left by removing 2 values

# # Example 1
# food = input("which food do you have? ")
# a = 30

#CLASSWORK: Create a program that would ask the user to supply a number. Determine whether the number is even or odd

# if food == "Rice":
#     print("i will buy rice")
# elif food == "Beans":
#     print("i will buy beans")
# elif food == "Yam":
#     print("i will buy yam")
# else:
#     print("i will not buy any food")


# user_number = int(input("Enter your number "))

# if user_number % 2 == 0:
#   print("This is an even number")
# else:
#   print("This is an odd number")

# ASSIGNMENT:
# Create a python program that would ask user to supply their first value, second value and the arithmetic operation the user would like to perform. i.e if the user enters "+", your program should perform first val plus second val. Do this for the remaining arithmetic operations.

# STRINGS

# # Python String Class
# name = ('sunday') #they are characters and always in quote
# val = str(10)

# name3 = """My name is faith and i am very very stubborn
# """ #is either use 'faith' or this "faith" or this """faith"""
# name4 = "faith's car"
# val = "10"
# print(val)
# print(type(val))
# print('i am ' + val + ' years old')
name2 = 'Monday'
name = 'pythonorest'
# print(name[2])
# print(name[3])
# print(name[:])
# print(name[2:])
# print(name[:4])
# firs = name[:4]
# print(name[6:])
# print(name)
# print(type(name))
# print(name[4])
# print(name[2:6])
# print(name[:])
# print(name[:7])
# print(name[3:])

# print(name[-4])
# print(name[-4:])
# print(name[:-4])
# print(name[:-1])
# print(name[-1:])
# print(name[-6:-1])
# print(name[:-5])
# print(len(name))

# print(name[4])
# print(name[:5]) #this numbers are index numbers. String can be sliced, you can request for numbers from an index to an index, this process is called slicing
# print(name[-3:])
# print(name[2])

name = 'pythonorest'

# print(name[-8: 10])
# print(name[1:6])
# print(name[3:-2])
# print(name[-10:-4])
# print(len(name)) #len means length of character or value
# name2 = "shade"
# name = "234567"
# print(name[2])
# print(name[-3:])
# print(len(name))

comment = """commented that This is a python class. it was started
#           last week and still continue through
#           this week. the number of people in this class is"""
# comment = "Definition: 'what is yor name?'"

# print(comment)
# print(len(comment))
# print(comment[27:39])
# print(comment[2])
# print(comment[0:9])
# print(comment[-2])
# print(comment[-30:-5])



# name = "supercalifragilisticexpialidocious"
# print(name[::2])
# name1 = "Disney"
# name2 = "sesquepedalian"
# print(name2[3:-2:3])
# print(name2[::-1])
# print(name2[1:9:2])

#ASSIGNMENT: Create a program that would ask the user to supply his phone number. If the phone number is up to 11 digits, generate an account number for the user (which would be the last 10 digits of his phonenumber).
#ASSIGNMENT2: Create a program that would ask the user to supply a word. Determine whether the word is a palindrome or not

# print(name2[6:-2:-2]) - #The negative step method in slicing won't return a value if it has been originally sliced negatively
# nam = "dali"
# print(nam[::-2])

# String Methods
# 
# nam = "Adeboyega"
# print(nam.startswith("Ad"))
# nam = input("Enter your name ")

# if nam.startswith("Ade"):
#   print("You are welcome")
# else:
#   print("Only the Ade family are allowed here")


# user_num = input("Enter your phone number ")

# if len(user_num) == 11:
#     print(f"Your account number is {user_num[1:]}")
#     print("Your account number is " + user_num[1:])
# else:
#     print("Your number must be 11 digits")

comment = """commented that This is a python class. it was started
# #           last week and still continue through
# #           this week. the number of people in this class is """

# print(comment.startswith('commented'))
# print(comment.startswith('we')) #comment here is the variable name, .startswith() is python in built function while "we" is the argument we are passing i.e. the word we are trying to find out.
# 
# print(comment.endswith("class is"))
# print("the length of comment is ", len(comment))

# comment = """    commented that This is a python class. it was started
# #           last week and still continue through
# #           this week. the number of people in this class is    """



# # # Strip() function
# nam = "   Ade"
# nam2 = nam.strip()
# print(len(nam))
# print(len(nam2))

# print('length before strip is ', len(comment))
# print('length after strip is ', len(comment.strip()))



# val1 = float(input("enter value 1 "))
# val2 = float(input("enter value 2 "))
# name = "addition"
# oper = input('enter operation: ')
# if oper.strip() == name:
#   print(val1 + val2)
# else:
#   print('Error')



# val1 = float(input("enter value 1 "))
# val2 = float(input("enter value 2 "))
# operation = input("Enter the operation you want to perform ").strip()
# if operation == "addition":
#     print(val1 + val2)
# else:
#     print("Error")



# Lower() function
# name = 'SUNDAY'
# print(name.lower()) # .lower() is used to transform all inputs by user to lowercase
# value = "login" #while using .lower(), your condition must be written in lowercase
# user = input("please enter login to continue: ").lower()
# if user == value:
#   print('welcome')
# else:
#     print("invalid input")

# Upper() function
# value = "LOGIN"
# user = input("please enter login to continue ")
# if value == user.upper():
#   print('welcome')
# else:
#     print("invalid input")

# # Replace() function
comment = """  commented that This is a python class. it was started last week and still continue through this week. the number of people in this class is   """

# newval = comment.replace("people", "student")
# newval = comment.replace("python", "django").replace("class", "school")

# print(newval)

# Split() function

# myval = "Adeola. bode. tayo. and bade are. my friends"
# print(myval.split("a"))
# print(myval.split("."))
# print(myval.split())

# print(comment.split())
# print(comment.split('.'))
# name = comment.replace('This', 'this')
# print(name)
# print(comment.split('week'))

# comment = """  commented that This is a python class. it was started
#           last week and still continue through
#           this week. the number of people in this class is   """

# # Join() function
# comment = """commented that This is a python class. it was started
# # #           last week and still continue through
# # #           this week. the number of people in this class is """


# word_split = comment.split()
# print(word_split)
# print(" ".join(word_split))
# value = ["rice", "beans", "yam", "banana"]
# print(value)
# print(" - ".join(value))
# # Capitalize() and Title function()
comment = """commented that This is a python class. it was started last week and still continue through
this week. the number of people in this class is  """
# 
# print(comment.capitalize())
# print(comment.title())

# bank = "Kuda"

# paul="i am coming\n pal"
# print(paul)

# Center() function
# print(comment)
# print(comment.center(200))

# Count() function
# print(comment.count("a"))

# Encode() function
# print(comment.encode())

comment = """commented that This is a python class. it was started
          last week and still continue through
          this week. the number of people in this class is  """

# In Operator
# val = "week" in comment
# print(val)
# val = "a" not in comment
# print(val)

# F METHOD
# name = input('Enter the name: ')
# num = int(input('Enter the number of student: '))


# comment = f"""{name} commented that This is a python class. it was started
#           last week and still continue through
#           this week. the number of people in this class is {num}"""
# print(comment)


comment = f""" commented that This is a python class. it was started
          last week and still continue through
#           this week. the number of people in this class is """
# yes = comment.split()
# print(yes)
# print(type(yes))
# print('Let Append')
# name = []
# firstname = ["firstname", "lastname", "age"]
# for first in firstname:             #first here will extract the values of firstname one after the other
#     names = input("Enter your " + first + " ")
#     print(names)
#     name.append(names)
# print(name)

# chose = input('Enter the word u want to append: ')
# yes.append(chose)
# print(yes)
# print('Let Insert')
# chose_new = input('Enter the word u want to insert: ')
# chose_n = int(input('Enter the index: '))
# yes.insert(chose_n, chose_new)
# print(yes)
# print(comment)
# new = input('Enter new word: ')
# com = comment.replace('python', new)
# print(com)
# print(comment.format(name, num))
# print(comment)


# Escape character
# print('she\'s is the owner paul says and i quote "GOD IS GOOD" ')
# print('she\'s the best')
# print('she\'s ')
# print("she's")
# print('she is the\b owner\b ')
# print('she is the\t owner')

# student_name= ["Abimbola", "Akin", "Kola", "Sewa", "Ade", "Seun"]
# Array:
#     list
#     tuple
#     set
#     dictionary
# []
# list()
# names = {"sola", "sade", "tunde", "bunmi"}
# print(names)

# List: is a collection which is ordered and changeable.
#  A list is created with a square bracket [] or list() constructor.
myFirstName = "ade"
mySecond = "shola"
myThird = "ayo"


# myNames = ["ade", "shola", "ayo"]

# randomThings = ["hey", 1, True, 5.8, ["open", 2]]


randomThings2 = list(("hey", 1, True, 5.8))

my_list = ["Shade", "energy", "magnet", "Charse", "power"]
my_list2 = list((12, 14, "Sunday", "Charse", True, False, 5.08))
my_list3 = [1, 45, 54, 23, 67, 78, 46]


# print(my_list)
# print(type(my_list))

# print(type(my_list2))

# print(my_list[3])

# my_list[3] = "Victor"
# print(my_list)


# my_list[1] = "solar"
# my_list[-2] = 'paul'
# print(my_list)
# print(my_list[0:3])
# print(my_list2[-3])
# print(my_list[-4:-1])
my_list = ["Shade", "energy", "magnet", "Charse", "energy"]
# print(len(my_list))
# # print(type(my_list2))
# if "Shade" in my_list:
#   print("present")
# else:
#   print("not available")

# 

my_list = ["Shade", "energy", "magnet", "Charse", "energy"]
my_list2 = list((12, 14, "Sunday", "Charse", True, False, 5.08))
my_list3 = [1, 45, 54, 23, 67, 78, 46]
# my_list.append(250)
# my_list.append(400)
# print(len(my_list))
# print(my_list)

# my_list.insert(3, my_list2)

# print(my_list)
# print(my_list[3][3])
# my_list.extend(my_list2)
# print(my_list)
# my_list.append(my_list2)
# print(my_list)
# print(my_list)
# print(my_list)

# for val in my_list: #This is a for loop. It is outputing each of the items in my_list
#   print(val)

# my_list = ["Shade", "energy", "magnet", "Charse", "energy"]


# if "my girlfriend" in my_list:
#     print("I love you")
# else:
#     print("She's too classy to be seen amongst common people.")

# acceptedword = []
# user_inp = input("Enter the password ")

# if user_inp == "ade":
#     acceptedword.append(user_inp)
#     print("Correct")
#     print(acceptedword)
# else:
#     print("This is an invalid password")

# my_list.remove("Shade") # remove is an inbuilt attribute of python object
# print(my_list)
my_list = ["Shade", "energy", "magnet", "Charse", "energy"]
my_list2 = list((12, 14, "Sunday", "Charse", True, False, 5.08))
# my_list2.pop(3)

# print(my_list2)
# my_list2.pop() #This will remove the last item since the inde is not specified
# print(my_list2)
my_list = ["Shade", "energy", "magnet", "Charse", "energy"]
my_list2 = list((12, 14, "Sunday", "Charse", True, False, 5.08))
my_list3 = [1, 45, 54, 23, 67, 78, 46]
# my_list2.clear()
# print(my_list2)
# del my_list2
# print(my_list2)

# user_num = input("Enter your phone number ")
# if len(user_num) == 11 and (user_num.startswith("0802") or user_num.startswith("0808")):
#     print("Your network is airtel")
# elif len(user_num) == 11 and (user_num.startswith("0805") or user_num.startswith("..")):
#     print("Network is glo")
# else:
#     print("Please enter a valid phone number")

# my_list3.sort()
# print(my_list3)
# my_list3.sort(reverse=True)
# print(my_list3)
my_list = ["Shade", "shade", "Energy", "Ola", "Charse", "energy" , "ola"]
# my_list.sort(reverse=True)
# my_list = ["ade", "Bade", "dayo", "Shade"]
# my_list.sort()
# print(my_list)
# my_list.sort(key=str.lower)

# print(my_list)


my_list = ["shade", "energy", "magnet", "Charse", "energy"]
my_list2 = list((12, 14, "Sunday", "Charse", True, False, 5.08))
my_list3 = [1, 45, 54, 23, 67, 78, 46]
# print(my_list3)
# print(type(my_list3))
# con = tuple(my_list3)
# print(con)
# print(type(con))
# my_list3.sort(reverse=True)
# my_list3.reverse()
# print(my_list3)
# name = my_list2.copy()
# print(name)
# name = list(my_list2)
# print(name)
# name = my_list + my_list2
# print(name)
# print(my_list.count("energy"))
# print(max(my_list3))
# print(min(my_list3))
# my_list = ["Shade", "energy", "magnet", "Charse", "energy"]
# print(my_list.index("magnet"))

# li4 = ["ad", 1, True, "df"]
# print(2 + li4.index("df"))
my_list = ["Shade", "energy", "magnet", "Charse", "energy"]
my_list2 = list((12, 14, "Sunday", "Charse", True, False, 5.08))
my_list3 = [1, 45, 54, 23, 67, 78, 46]
my_list4 = [my_list, my_list2, my_list3, ['Favour', 34],my_list2, 'Tunde', False]


# print(my_list4)
# print(my_list4[3][-1])
# print(my_list4[4][4])
# print(my_list4[-4:-1])
# print(my_list4[-6:-2:2])

# my_list[0] = "temmy"
# print(my_list)
# 
# username = ["ade", "bade"]
# passw = ["o1", "de"]
# position = username.index("ade")
# print(passw[position])
score = 0
questions = ["1. Who is the president of Nigeria?", "2. Who is the president of CBN?", "3. What is the name of the vice president of Nigeria?"]
options = ["a. President Umar Musa Yar'adua \n b. President Goodluck Ebele Jonanthan \n c. President Muhammad Buhari", "a. Godwin Ewemiewele \n b. Godwin Ewefiele \n c. Godwin Emefiele", "a. Joe Biden \n b. Yemi Osinbajo \n c. Jide Sanwoolu"]
answer = ["c", "c", "b"]
# usernm = input("ENter your username ")
# for quest in questions:
#     print(quest)
#     position = questions.index(quest)
#     print(options[position])
#     user_ans = input('Enter your answer ').lower()
#     correct_answer = answer[position]
#     if user_ans == correct_answer:
#         score += 10
# print(f"Dear {usernm}, you scored {score}")

# myNames = ["Ade", "Shola", "Muyiwa"]

# print(myNames)
# print(myNames[0])
# print(myNames[1])
# print(myNames[2])

# for something in myNames:
#   print(something)
#   aa = input("Enter your answer")

# score = 0
# questions = ["1. Who is the president of Nigeria?", "2. Who is the president of CBN?", "3. What is the name of the vice president of Nigeria?"]
# options = ["a. President Umar Musa Yar'adua \n b. President Goodluck Ebele Jonanthan \n c. President Muhammad Buhari", "a. Godwin Ewemiewele \n b. Godwin Ewefiele \n c. Godwin Emefiele", "a. Joe Biden \n b. Yemi Osinbajo \n c. Jide Sanwoolu"]
# answer = ["c", "c", "b"]

# for val in questions:
#     print(val)
#     valid = questions.index(val)
#     print(options[valid])
#     user_ans = input("Enter your answer ")
#     if user_ans == answer[valid]:
#         score += 5
# print(f"Your score is {score}")

# Tuple: A tuple is a collection that is ordered but not changeable.
# A tuple is created using
#  braces i.e () or tuple()
mytuple = ("ade", "femi")
my_list = ["ade", "femi"]
# my_list[0] = "Tope"
# print(my_list)
# mytuple[0] = "Tope"
# print(mytuple)
name = ("Shade", "energy", "magnet", "Charse", "energy")
name2 = tuple((12, 14, 1, "Sunday", "Charse", False, 5.08))
# print(name[2])
# print(name)
# print(type(name))
# print(name2)
# print(type(name2))
# print(name[3])
# print(name[1:4])
# print(name[-3])
# print(name[-3:-1])
# print(len(name))
# print(name.index("magnet"))
# food = ('Yam',)
# print(food)
# print(type(food))
# if "True" in name2:
#   print("is available")
# else:
#   print('not available')
# print(name)
name = ("Shade", "energy", "magnet", "Charse", "energy")
nm = list(name)
nm2 = ["Shade", "energy", "magnet", "Charse", "energy"]
nm3 = {"Shade", "energy", "magnet", "Charse", "energy"}
# print(type(name))
# print(type(nm))
# name.pop()
# print(name)
# print(name)
# nm2.append("Adesewa")
# name.append("Adesewa")
# print(name)
# nm2[3] = 'wine'
# name[3] = 'wine'
# nm.append("toy")
# print(nm)
# print(nm)
# name[3] = "wine"
# print(name)
# nm3.add('Sade')
# print(nm3)
# name.add("toy") # tuple has no attribute add error
# name.pop() # tuple has no attribute pop error
# name = ("Shade", "energy", "magnet", "Charse", "energy")
# del name
# print(name)

# Unpacking values of a tuple
item = ("Ola", "22", "07064203742")
# name, *others = "Ola", 22, 7064203742, "Sewa", "Abimbola"
# print(name)
# print(others)
# (name, *phonenumber) = item
# print(phonenumber)
item = ("Yam", "Sunday", "Lagos", "Yam", "Sunday", "Lagos", 45)
# (food, name, *location, age) = item
# print(age)
# print('food: '+ food)
# print(f'location: {location}')
# print(len(item))
# (food,  *name, age, mymy, our) = item
# print(name)
# (*name, ) = item
# print(name)

# for na in item:
#   print(na)
name = ("Shade", "energy", "magnet", "Charse", "energy")
name2 = tuple((12, 14, 1, "Sunday", "Charse", False, 5.08))
# new_name = name + name2
# print(new_name)
# print(type(new_name))
# new_name = name * 3
# print(new_name)
# print(name.count("energy"))
# name = ("Shade", "energy", "magnet", "Charse", "energy")
# name2 = tuple((12, 14, 1, "Sunday", "Charse",False, 5.08))
# print(name.index("magnet"))

fruits = ('Name', 'name', 'age', 12, 'Age')
# print(fruits.index('name'))


# Set: A set is a collection which is unordered and unindexed.
#  It is written using curly bracket
# It doesn't accept duplicates
# i.e {} or set()
name = {"Shade", "energy", "magnet", "Charse", "Charse", "energy"}
name2 = set((12, 14, "Sunday", "Charse", True, False, 5.08))
# print(name)
# print(name[2])
# print(name2)
# print(len(name))

# print(type(name2))
# for top in name2:
#     print(top)
# print("Charse" not in name)
# print("student" not in name)
# name.add("orange")
# print(name)
# name.update(name2)
# print(name)
# name.add("seun")
# print(name)
name = {"Shade", "energy", "magnet", "Charse", "Charse", "energy"}
new_name = ["food", "drink", "dress", "wears"]
# name.update(new_name)
# print(name)
# print(type(name))
name = {"Shade", "energy", "magnet", "Charse",  "Charse", "energy"}
name2 = set((12, 14, "Sunday", "Charse", True, False, 5.08))
name.update(("mango", "apple", "leave"))
# print(name)
# print(type(name))
name = {"Shade", "energy", "Charse", "magnet", "energy", "see"}
# # name2 = set((12, 14, "Sunday", "Charse", True, False, 5.08))
# name.remove("see")
# print(name)
val1 = 2
# val = set()
name = {"Shade", "energy", "Charse", "magnet", "energy", "see"}
# name.discard("see")
# print(name)
# name.pop()
# print(name)
# name.clear()
# print(name)
# del name
# print(name)
name = {"Shade", "energy", "Charse", "magnet", "energy"}
# name2 = set((12, 14, "Sunday", "Charse", True, False, 5.08))
# for y in name:
#   print(y)
#   print(type(y))

# set1 = {1, 90, 2}


comment = f""" commented that This is a python class. it was started
         last week and still continue through
        this week. the number of people in this class is """
# new = comment.split()
# print(new)
# t = tuple(new)
# # print(t)
# s = set(t)
# print(s)
# new_input = set(input('Enter here: ').split())
# print(new_input)
# print(yes)
# yes = {6, 1, 2, 3, 4, 5}
# s = {1, 4, 5}
# inter = s.intersection(yes)
# print(inter)
set1 = {2, 8, 6, 4}
set2 = {2, 4, 50, 5, 7, 8,12, 13}

set3 = {20, 50, 60}

# set4 = set1.union(set2).union(set3)
# print(set4)
# set3.update(set2)
# print(set3)
# print('Set1:', set1)
# print('Set2:', set2)
# print('Set3:', set3)
# intercept = set1.intersection((set2))
# print(intercept)
intercept = set1.intersection((set2)).intersection((set3))
# print(intercept)
# set1.update(set2)
# print('Result:', set1)

set2 = {2, 4, 50, 5, 7, 8,12, 13}
set1 = {10, 50, 3, 4}
set3 = {10, 3, 4, 20, 50, 60}
# set4 = set1.symmetric_difference(set2)
# print(set4)
# print('s_d:', set4)
# print(set2)
# set2.symmetric_difference_update(set1)
# print(set2)
# print('s_d_update:', set2)
set4 = set3.intersection(set1)
set5= set3.symmetric_difference(set1)
# set3.difference_update(set1)
# set3.symmetric_difference_update(set1)
# print(set3)
# print(set4)
# print(set5)
set2 = {2, 4, 50, 5, 7, 8,12, 13}
set1 = {10, 50, 3, 4}
set3 = {10, 3, 4, 20, 50, 60}
# print(set1.isdisjoint(set2)) #This will return False if an intersection can be made
# print(set1.issubset(set3)) #This will check whether set1 is the child of set3
# print(set3.issuperset(set1)) #This will check whether set3 is the parent of set1

s1 = {1, 2, 3}
s2 = {1, 2, 4}
# s3 = s1.symmetric_difference(s2)
# print(s3)
# s2.symmetric_difference_update(s1)
# print(s2.intersection(s1))
# print(s2)


# for i in range(3):
#     print("Hello")


# c = []
# f = []
# for i in range(3):
#     a = int(input('a: '))
#     c.append(a)

# for m in range(3):
#     b = int(input('b: '))
#     f.append(b)
# j = set(c)
# k = set(f)
# print(c)
# print(f)
# print(j)
# print(k)
# intercept = j.intersection((k))
# print(intercept)
# union = j.union((k))
# print(union)
# if intercept == set():
#     print('Intersection: ', 'Empty set')
#     print('Union: ', union, "my result")
# else:
#     print('Intersection: ', intercept)
#     print('Union: ', union)


# Dictionary: Dictionary is a collection which is ordered, changeable but does not allows
# duplicate and unindexed. Dictionary are used to store data in a key:value pairs.
# # It is written using {key:value} or dict(key=value)
# myNames = ["Ade", "boola"]
# myNames = {
#     "firstname" : "ade",
#     "secondname" : "shewa"
# }

# print(myNames["firstname"])
product = {
    "producer": "Toyota",
    "model": "venza 2021",
    "engine": "6 engine",
    "color": "black",
    "gear": 6,
    "ok": True,
}

# print(product["color"])
# myNames = {"Name1": "Nath", "Name2":"Michael"}
# print(myNames["Name1"])

# student_info = {1234: ["Taofeeq", "12", "Data science"]}
# print(student_info[1234])

# student_record = {"Isaac":["Male", 23, "Single to stupor"], "Taofeeq":["Male", 20, "Every lady is my goal"]}
# print(student_record["Taofeeq"][-3])

# s_r = {2035: ["Male", "Datascience", 12, 4, True]}

student_record = dict(
    name="Tony Johnson", level=300, course="mechanical engineering", subjects=10
)
# print('Student_record:', student_record)
# print(product)
# print(len(product))
# print(type(product))
# print(product["model"])
# print(product.get("model"))

# print(product.keys())
# print(product.values())

# product = {
#     "producer": "Toyota",
#     "model": "nath 2026",
#     "engine": "6 engine",
#     "color": "black",
#     "gear": 6,
#     "ok": True,
# }

# product["passenger"] = "ten"
# product["producer"] = "Nath"
# print(product)

# product["tyres"] = "4"
# print(product)
# print(student_record.items())
# print(student_record)
product = {
    "producer": "Toyota",
    "model": "venza 2021",
    "engine": "6 engine",
    "color": "black",
    "gear": 6,
    "ok": True,
}
student_record = dict(
    name="Tony Johnson", level=300, course="mechanical engineering", subjects=10
)
# print(student_record.values())
# print(0 not in student_record.values())
# product["engine"] = "lexus engine"
# product["air conditioner"] = "yes"
# product["producer"] = "lexus producer"
# print(product)
product.update({"year":2021, "color":"white", "speed": "500mph", "ok":False, "model": "Benz 2022"})
product["year"] = 2021
# print(product)
# product.pop('color')
# print(product)
# student_record.pop('course')
# print(student_record)
# print(product)
# product.popitem()
# print(product)
# del product["color"]
# print(product)
# product.clear()
# print(product)
# del product
# print(product)
# print(student_record)
product = {
    "producer": "Toyota",
    "model": "venza 2021",
    "engine": "6 engine",
    "color": "black",
    "gear": 6,
    "ok": True,
}
# student_record = dict(
#     name="Tony Johnson", level=300, course="mechanical engineering", subjects=10
# )
# print('Student_record:', student_record)

# for i in product:
#   print(i)

# for i in product:
#   print(product[i])
# for x in product.values():
#   print(x)
# for x in product.keys():
#   print(x)

# for x, y in product.items():
#     print(f"{x} :  {y}")
#     print("Hello")


# new_record = product
# print(new_record)
# new_record = dict(student_record)
# print(new_record)
student_details = {
  "Tony Johnson":{'name':'Tony Johnson', 'level':400, 'location':'Takie',
'dept':'math'},
  "Micheal Chan":{'name':'Micheal Chan', 'level':200, 'location':'General',
'dept':'computer'},
"Timi Joy":{'level':400, 'location':'Apake', 'dept':'english'}
}
# print(student_details.keys())
std1 = {'name':"Tony Johnson", 'level':300, 'location':'Takie', 'dept':'math'}
std2 = {'name':"Micheal Chan", 'level':200, 'location':'General', 'dept':'computer'}
student_details2 = {
  'FIRST_PERSON':std1,
  'SECOND_PERSON':std2
}
# print(student_details2['FIRST_PERSON'])
# print(student_details["Tony Johnson"])
# print(std1)
# print(student_details["Micheal Chan"]['location'])
# for record in student_details2['FIRST_PERSON']:
#   print(record)
# for record in student_details["Tony Johnson"].values():
#   print(record)

# ASSIGNMENT: Create a phonebook program that would allow the following operations: 1) Viewing the phonebook, 2) Adding to the phonebook 3) Deleting from the phonebook
