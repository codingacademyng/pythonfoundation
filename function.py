# import random
# print(random.random())
# myList = ["red", "blue", "green", "lack"]
# print(random.choice(myList))
# print(random.randint(100, 9000))

# STAGES OF FUNCTION:
# function declaration: def funcitonName(): or def function_Name(param_a, param_b):
# function definition: print("This is a function to print something to screen")
# function invocation: functionName() or function_name(value_a, value_b)

# def sayHello():
#     print("Hello")
#     print("hi")
#     for i in range(3):
#         print(i)
# sayHello()
# def name(): #this is function declaration
#     na = "maya"
#     print(na) #this is function definition
# name()# this is function invocation

def sayHello():
    print("Hello world")
    print("Today is monday")
    print(2 + 2)

# sayHello()
# val1 = 50
# val2 = 20

# def addition():
#     # this is to add two function together
#     result = val1 + val2
#     print(result)

# addition()
# val1 = 20

# def multiply():
#     global val2
#     val1 = 20
#     val2 = 10
#     print(val1 * val2)
# multiply()

# print(val2)

# val1 = 50
# val3 = 23

# def algebra1():
#     global val3
#     val3 = 35
#     res = val1 + val3 * 5
#     print(res)

# algebra1()
# print(val3)

# def subtraction():
#     result = val1 - val3
#     print(result)
# subtraction()

# algebra1()
# subtraction()
# Parameterized and non-parameterized function
# non-parameterized function - without parameter or 
# arguments
#  example:
# def name():
#     print('Nath')
# name()
# parameterized function - function with parameter/argument:

# form of parameterized function
# required argument- the number of argument should be the same in both f.call and f.declaration
# position should be followed

# # Example:
def display(x, y, z):
    print(x)
    print(y)
    print(z)


# display(10, 20, 5) #this means that the number entered in the function def should be the same in the function call.

# display(4, 3, 10)

def addAndMultipy(num1, num2, num3):
    res = num1 + num2
    print(res * num3)
# addAndMultipy(2, 4, 5)
# addAndMultipy(8, 4, 5)
# num1 = int(input("Enter first number "))
# num2 = int(input("Enter first number "))
# num3 = int(input("Enter first number "))
# addAndMultipy(num1, num2, num3)

def home():
    val1 = int(input("Enter val 1 "))
    val2 = int(input("Enter val 2 "))
    inp = input("What operation would you like to perform ")
    if inp == "1":
        addition(val1, val2)
    elif inp == "2":
        subtraction(val1, val2)
    else:
        print("bye bye")

def addition(a, b):
    print(a + b)
    home()

def subtraction(a, b):
    print(a - b)
    home()


# def sayHello():
#     print("hello")

# def navigate():
#     inp = input("Enter your operation ")
#     if inp == "1":
#         sayHello()
# sayHello()
# navigate()
    
# Keyword argument - order/position is both required
# initialization is done based on the keyword

def faith(x, y):
    print(f"Variable y is {y} and variable x is {x}")

# faith(20, "shade")

# faith("ay", "precious")
# faith(y="Ay", x="Precious") #in keyword argument, position is not required, just the keyword.

# faith(y= 30, x=15)
# Default argument - the number of arguments need not to be matched with both f.call and f. def
# some argument will be considered as defualt argument.

def display(name='maya', course='Datascience', level='2'):
    print(name, course, level)
    
# display(name = 'ola', course = 'Web Development') #this will overright whatever you have in your argument.
# display(name = 'gbenga')
# display() #this will change the name to the new name and pick the otherwise

# Variable Length Argument- arbitruary number of arguments and it is done by placing * as prefix to the argument of the f.def
# def display(course, thing, *something):
#     print(course)
#     print(thing)
#     print(something)
# display('Datascience', 'Data Analysis', 'Web Development', 'Graphic dsign', 20)

# def addition(val3=40,  val4=34):
#     result = val3 + val4
#     print(result)

# addition(val3=20)

# def subtract(val3, val4=34):
#     print(val3 - val4)

# subtract(50, 30)

#ASSIGNMENT: Segment your cbt, phonebook and registeration assignments into their respective functions and allow the user to navigate in those assignments.

# Return function
# A return statement is used to end the execution of function call and "retuns" the result
# (value of the expresion yfollowin the return keyword) to the caller.
# example

# def test(a, b):
#     result = a + b
#     return result
# print(test(9, 9))
# val1 = test(9, 10)
# val2 = 20
# print(test(5, 30))
# val2 = test(5, 30) + 30
# print(val2)

# def add(a, b):
#     sum = a + b
#     return sum

# a = int(input('Enter your first value: '))
# b = int(input("Enter your second value "))
# res = add(a, b)
# print(f"The result is {res}")

# a = 50
# b = 20
# def subtract(a, b):
#     return a - b
# print(subtract(a, b))



# def subtract(a, b):
#     return a - b

# def addition(val3, val4):
#     res = val3 + val4 + subtract(int(input('subt value a >> ')),  int(input("Subt value b >> ")))
#     return res
# print(addition(10, 20))

# val1 = 50
# val2 = 20
# def addition(a, b):
#     return a + b


# def myName():
#     name = input("Enter your name ")
#     return name

# def algebral():
#     add = addition(int(input('add value 1  ')), 10)
#     result = (val1 + val2) * add
#     print(f"Welcome {myName()}  your score is {result}")
# algebral()
"""
Assignment

Write a simple python program that will ask user to login, after login, user
should be able to choose operation to perform.
If user decides to do calculations, open calculation for the user,
if it is set, open sets
if it is cbt, open cbt for the user.
NOTE: 
User's username should be in database before they can login;
User's username must match with the password to login,
User should be able to perform Addition, Subtraction, Multiplication and Division operations under Calculation
User should be able to do cbt under cbt operation
User should be able to supply sets and perform all sets operation under sets.
FURTHER:
When user is done with any operation, user should be able to perform another operation
user can also decides to logout

"""
import sys
import time

# #solution
# def login():
#     dbusername = ["sade", "bunmi", "bola"]
#     dbpassword = ["1234", "5678", "0912"]
#     username = input("Supply username ")
#     pwd = input("Supply password ")
#     if username in dbusername and pwd == dbpassword[dbusername.index(username)]:
#         print("Confirming login details")
#         time.sleep(2)
#         print("Login successful")
#         operation()
#     else:
#         print("Login failed, try again")
#         time.sleep(2)
#         login()

# def operation():
#     print("""
#     These are the operations you can perform:
#     1. CBT
#     2. CALCULATIONS
#     3. SET
#     4. LOGOUT
#     5. CLOSE APPLICATION
#     """)
#     task = input("Enter a number to perform operation ")
#     if task == "1":
#         exam()
#     elif task == "2":
#         calculations()
#     elif task == "3":
#         set_operation()
#     elif task == "4":
#         time.sleep(2)
#         login()
#     elif task == "5":
#         time.sleep(2)
#         sys.exit()

#     else:
#         print("Invalid input")
#         time.sleep(2)
#         operation()

# def exam():
#     global score
#     score = 0
#     nt = 0
#     questions = ["1. What is the full meaning of ECOWAS", "2. SQI is which type of school?", "3. Who is the president elect in the just conclude 2023 election?",
#                  "4. Which of these is an odd word?", "5. Which of this is not python in built function?", "6. What is the correct question tag for this statement 'we have been looking for you'",
#                  "7. Python is a ____ language?", "8. How many states do we have in Nigeria?", "9. Center of Excellency is to Lagos as ___ is to Ondo?",
#                  "10. Who won the 2022 World Cup?"]
#     options = ["a. Economic Community of West African States \n b. Economic Common Wealth And Sales \n c. Economic Common Wealth of West African States",
#                "a. Business School \n b. Coding School \n c. Army School", "a. President Muhammad Buhari \n b. Prof. Yemi Osinbajo \n c. Bola Ahmed Tiubu",
#                "a. Fertilization \n b. Ovulation \n c. cultivation \n d. Reproduction", "a. lower() \n b. print() \n c. input() \n d. create_account()",
#                "a. haven't they? \n b. haven't we? \n c. hadn't we?", "a. progamming language \n b. igbo language \n c. traditional language",
#                "a. 36 \n b. 37 \n c. 38", "a. Food Basket of the Nation \n b. Pearl of Tourism \n c. Sunshine State", "a. Nigeria \n b. France \n c. Argentina"]
#     answer = ["a", "b", "c", "c", "d", "b", "a", "a", "c", "c"]
#     for que in questions:
#         print(que)
#         time.sleep(2)
#         print(options[nt])
#         time.sleep(1)
#         ans = input("input your answer >>> ")
#         an = answer[nt].lower()
#         if ans == an:
#             print("Correct")
#             score +=10
#         else:
#             print("You are wrong")
#             score -= 5
#         nt +=1
#     print("Your total Score is " + str(score))
#     print("Enter 1 to perform another operation..\n Enter 2 to logout..\n #nter 3 to take exam again\n Enter 4 to exit..")
#     another = input(">>> ")
#     if another == "1":
#         operation()
#     elif another == "2":
#         login()
#     elif another == "3":
#         exam()
#     elif another == "4":
#         sys.exit()
# def calculations():
#     print("Which calculation will you like to perform?")

# def set_operation():
#     print("This is for set operation")

# login()

"""
Write a python program for student registration portal that will ask user to register and give matric number to the student.
NOTE:
- Your code should be able to generate matric number for the student.
- if admin did not enter "end", admin should be able to keep registring students;
- at the end of the registration process, your code should be able to fetch the student details and matric number
- your code should be able to print all matric numbers of students registered.
"""

# users = ["ade"]
# passwords = ["12ad"]

# def home():
#     resp = input("Welcome to nath's app. Enter 1 to login oor 2 to register ")
#     if resp == "1":
#         login()
#     elif resp == "2":
#         register()

# def register():
#     username = input("Enter your username ")
#     passw = input("Enter your password ")
#     print('Registration successful')
#     users.append(username)
#     passwords.append(passw)
#     print(users)

# def login():
#     username = input("Enter your username ")
#     passw = input("Enter your password ")
#     if username in users and passw in passwords:
#         if users.index(username) == passwords.index(passw):
#             print("login successful")
#         else:
#             print("Invalid details, try again")
#             login()
#     else:
#         print("Invalid details, try again")
#         login()

# home()