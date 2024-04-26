# Python loop is used to execute a block of code repeatedly
# python loop used in a situation whereby you want to make 
# use of a piece of code over and over but you don't want to write the same code multiple times
# FOR loop is used for iterating over a sequence

# FOR LOOP

# print("Hello")
# print("Hello")
# print("Hello")
# rag = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# for damola in range(9):
    # print(damola)
    # print("Hello")
    # print(2 + 2)
#     print(2 * damola)
# print("Something")

# myNum = 4

# for i in range(3):
#     myNum += i

# print(myNum)

# for i in range(9):
#     print("Hello")
#     print("hi")
#     print(i)
# print("some")

# my_ = ['shade', 'energy', 'Magnet', 'Charse', 'Energy']


# for name in my_:
#     print(name)
#     print("Hello")
# print("Ebun asked me to type something")

# my1 = "shade"
# my2 = "energy"
# my3 = "charse"
# m4= "magnet"
# m5 = "Energy" # for loop can easily help us reduce this type of multiple lines of codes
# print(my1)
# print(my2)
# print(my3)
# print(m4)
# print(m5)

# myLo = ["Ade", "Shade", "Bade", "Imade", "Fade", "Molade"]
# print(myLo[0:600:2])
# for x in range(10):
#     print(x)

# evenNum = []
# for i in range(2, 31, 2):
#     evenNum.append(i)
# print(evenNum)
    

# num = []
# for x in range(0, 20, 3):
#     print(x)
#     num.append(x)
# print(num)

# num = []
# for x in range(0, 20, 2):
#     print(x)
#     num.append(x)
# print(num)

# for i in range(6):
#     print(i)
#     if i == 3:
#         break

# for i in range(7):
#     if i == 4:
#         continue
#     print(i)
#     print("Hellp")

# my = ['Shade', 'energy', 'Magnet', 'Charse', 'Energy']
# for name in my:
#     if name == my[-3]:
#         continue
#     print(name)
  
# for i in range(20, 1, -1):
#     print(i)

# asi = 1
# put = input("Which symbol would you like to use ")
# def go(ans, put):
#     ansi = ""
#     for x in range(ans):
#         ansi += put
#     ans += 1
#     print(ansi)
#     if x <= 20:
#         go(ans + 1, put)
# go(asi, put)

# num = []
# user_inp = input("Enter a symbol ")

# for x in range(20):
#     num.append(user_inp)
#     print("".join(num))

# user_inp = input("Enter a symbol ")
# for i in range(0, 40, 3):
#     x = i * user_inp
#     print(x)

# user_inp = input("Enter a symbol ")
# li = []
# for i in range(0, 50, 3):
#     li.append(user_inp)
#     print("".join(li))

# for i in range(0, len(li)):
#     li.pop()
#     print("".join(li))

# user_inp = input("Enter a symbol ")
# for i in range(20):
#     print(i * user_inp)

# import time
# position = 0
# score = 0
# question = ["Who is the president of Nigeria?", "SQI is which School?", "Which language is python?"]
# answer = ["President Muhammad Buhari", "Business School", "Programming Language"]
# for que in question:
#     print(que)
#     time.sleep(2)
#     ans = input("Enter your answer ").title()
#     correct = answer[position]
#     if ans == correct:
#         print("Youre right")
#         score +=5
#     else:
#         print("You are wrong")
#     time.sleep(2)
#     position +=1
# print(score)

# for anything in range(10):
#   print("Hello")
#   print("Hi")
#   print(anything + 5)
#   print(anything)

# for anything in range(9):
#   if anything == 5:
#     print(anything + 5)

# usernames = []
# passwords = []

quest = ["what is my name", "sdefer"]
options = ["a) Ade\nb) Shade\nc) Dayo", "a) ujhyh\nb) jhgfd\nc) tgfrfg"]
answers = ["a", "b"]

# for i in range(5):
#   username = input("Enter your username ")
#   password = input("Enter your password ")
#   usernames.append(username)
#   passwords.append(password)
# print(usernames)
# print(passwords)


# result = []
# for i in range(5):
#   inp = input("enter any number>> ")
#   result.append(inp)
#   print(result) #this indentation here will be printing at every stage of iteration

# students = []
# for i in range(5):
#     name = input("Enter your name ")
#     students.append(name)
# print(students) #this indentation here will print at the end of iteration
students = set()

# for i in range(3):
#     x = []
#     enter = input("Enter your name ")
#     x.append(enter)
#     students.update(x)
# print(students)


# theory questions


# NESTED FOR LOOP
# import time

# for i in range(8):
#     print(i)
#     time.sleep(2)
#     for j in range(9):
#         print(j)
#         time.sleep(1)


# names = ["Sunday", "Samson", "Johnson", "Marian", "Lydia", "Young", "Peter"]
# fruits = ["Mango", "Cashew", "Pineapple", "Orange"]
# for name in names:
#     print(name, " is picking his own fruit")
#     for fruit in fruits:
#         print(fruit)
#         # if name == "Sunday" and fruit == "Cashew":
#         #     break
#         print(f"{name} has picked {fruit} fruit")


import time
question = ["Who is the president of Nigeria?", "SQI is which School?", "Which language is python?"]
answer = ["President Muhammad Buhari", "Business School", "Programming Language"]

# student_scores = {}
# for i in range(3):
#     position = 0
#     score = 0
#     student_name = input('Enter your name ')
#     print("You can now proceed to your exam")
#     for que in question:
#         print(que)
#         time.sleep(2)
#         ans = input("Enter your answer ").title()
#         correct = answer[position]
#         if ans == correct:
#             print("Youre right")
#             score +=5
#         else:
#             print("You are wrong")
#         time.sleep(2)
#         position +=1
#     student_scores.update({student_name:score})
# print(student_scores)


# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

# myTup = (1, 2, 3, 4)
# multiplier = 1
# for i in myTup:
#     print(i * multiplier)
#     multiplier += 1


# for x in (1, 2, 3, 4, 5, 6, 7, 8, 9):
#     print("Multiplication Table", x)
#     for i in (1, 2, 3, 4, 5, 6, 7, 8, 9):
#         result = x * i
#         print(f"{x} * {i} = {result}")
#         print(str(x) + " * " +str(i) + " = " + str(result))

# numbers = [5, 2, 5, 3, 2, 1]
# for num in numbers:
#     output = ""
#     for item in range(num):
#         output += "x"
#         print(output)

# FINDING MAXIMUM NUMBER IN A LIST
# numbers = [3, 5, 6, 2, 1, 10, 14]
# max = numbers[0]
# for i in numbers:
#     if i > max:
#         max = i
#     print("the maximum number at each iteration is " + str(max))
# print(max)

# FINDING MINIMUM NUMBER IN A LIST?

# numbers = [20, 10, 5, 30, 4, 8]
# godAbeg = numbers[0]
# for item in numbers:
#     if item < godAbeg:
#         godAbeg = item
#     print("the minimum number at each iteration is " + str(godAbeg))
# print(godAbeg)
# iteration of summation of ranges
# numbers = range(1, 10)
# total = 0
# for number in numbers:
#     total += number
#     print(number)
#     print(f"The total is {total}")


# right_number = 4
# number_of_guesses = 3
# guess_count = 0
# print("You have 3 chances to choose a number between 0 and 9, after 3 attempts, this game will be terminated")
# while guess_count < number_of_guesses:
#     guess = int(input('Guess the right number: '))
#     guess_count += 1
#     if guess == right_number:
#         print("Correct, you won this game")
#         break
# else:
#     print('You have exceeded the number of times you can try')

# username = ["ola", "seun"]
# WHILE loop is used to run a block code until a certain condition is met.
# there can be nested for and nested while loops.

# a while loop evaluates condition if the condition evaluate to True, the code inside the while loop is executed
# the condition is evaluated again.
# This process continues until the condition is false.
# WHILE Loop
# # example

# while True:
#     print("Hello")

# x = 1
# while x <= 10:
#     print("You're welcome to class", x)
#     x += 2

# a = 5
# while a < 10:
#     print("Hello")
    

# < > != <= >= == =
# x = 10
# while x >= 1:
#     print("You're welcome to class", x)
#     x -= 1

# x = 10
# while x > 0:
#     x -= 1
#     if x == 5:
#         continue
#     print("I will not do it again", x)
    
    
# for x in range(10):
#     if x == 5:
#         continue
#     print(x)

# var = 10                    # Second Example
# while var > 0:              
#    var = var -1
#    if var == 5:
#       continue
#    print ('Current variable value :', var)
# print ("Good bye!")
# x = 10
# while x > 0:
#     print("I will not do it again", x)
#     x -= 1
# else:
#     print('Terminated')
# std_name = []
# x = 1
# while x < 10:
#     print("Enter q to quit")
#     name = input('Enter student name: ')
#     if name == 'q':
#         break
#     std_name.append(name)
#     x +=1
# print(std_name)
# print("Seun")
# phone = input('Enter phone number: ')
# while len(phone) != 11:
#     print("Phone number must be 11 digits")
#     phone = input('Enter phone number: ')
# else:
#     print("Phone number is valid")


# x = 10
# while x > 0:
#     x -= 1
#     if x == 5:
#         pass
#     print('You are welcome ', x)


# right_numbers = [0, 7, 9]
# no_of_attempts = 0
# correct_guesses = 0

# print("You are welcome to taofeeq's guessing game. You have only seven trials to get 3 numbers right between 0 - 10. Please note, you cannot guess the same right number twice")
# while no_of_attempts < 7:
#     user_inp = int(input("Enter your guess "))
#     if user_inp in right_numbers:
#         print("You are right")
#         correct_guesses += 1
#         right_numbers.remove(user_inp)
#     else:
#         print("You are wrong")
#     no_of_attempts += 1
#     if correct_guesses == 3:
#         break
#     print(f"You have {7 - no_of_attempts} trials left")

# if correct_guesses == 3:
#     print("Congratulations, you win having guessed the three nubers correctly")
# else:
#     print(f"You loose. You got only {correct_guesses} out of 3 numbers")

# x = 10
# while x > 0:
#     x -= 1
#     age = input('Enter your age: ')
#     if int(age) < 18:
#         print('You are too young to see this movie')
#         print(f"You have {x} trials left")
#     else:
#         print('Please take you ticket  and enter the hall')
#         break

# this interation will keep going as long as "d" is not entered
# def task():
#     x = input("input 'd' to stop ")
#     while x != "d":
#         age = input("Enter you age")
#         if int(age) < 18:
#             print('You are too young to watch this movie')
#         else:
#             print('Please take your cinema ticket and enter the hall')
#         x = input("input 'd' to stop ")
#     else:
#         print("Go home")
# task()

# x = input("input 'd' to quit ")
# while x != "d":
#     y = input("input 'terminate' to stop ")
#     if y == 'terminate':
#         break
#     age = input("Enter your age: ")
#     if int(age) < 18:
#         print("You are too young to watch this movie")
#     else:
#         print("Please take your cinema ticket and enter the hall", x)
# else:
#     print("Go home")

# user_inp = input("Enter stop to exit this program ").lower()

# while user_inp != "stop":
#     age = input("Enter your age: ")
#     if int(age) < 18:
#         print("You are too young to watch this movie")
#     else:
#         print("Please take your cinema ticket and enter the hall")

#     user_inp = input("Enter stop to exit this program ").lower()
# else:
#     print("Go home")

# name_list = []
# while True:
#     print('Type exit to quit at any time')
#     name = input('What is your name ')
#     if name == 'exit':
#         break
#     name_list.append(name)
# print(name_list)

# USSD
# ussd = input('Please enter ussd ')
# while ussd != '*131#':
#     ussd = input("Invalid input!!! please retry again ")
# no_of_trials = 5
# while ussd != '*131#':
#     if no_of_trials == 0:
#         break
#     ussd = input("Invalid input!!! please retry again ")
#     no_of_trials -= 1
# print('''
#         1. Daily Plan
#         2. Weekly Plan
#         3. Monthly Plan
#         4. Two Months Plan
#         5. Three months plan
#         6. Back
#     ''')

all_customer = {}

# for i in range(4):
    # firstname = input("Enter you firstname ")
    # lastname = input("Enter you lastname ")
    # age = input("Enter you age ")
    # phone = input("Enter you phone ")
    # while len(phone) != 11:
    #     print("Phone ust be 11")
    #     phone = input("Enter you phone ")
    # customer = [firstname, lastname, age, phone]
    # all_customer.update({f"customer {i + 1}":customer})
# i = 1
# while i <= 4:
#     customer = []
#     info = ["firstName", "lastName", "age", "phone"]
#     print("Enter customer " + str(i) + " information")
#     con = input("press 'enter' to continue or 'end' to quit ")
#     if con == "enter":
#         for fo in info:
#             inf = input("Enter your " + fo + ": ")
#             customer.append(inf)

#         while len(customer[3]) != 11:
#             print("Phone number must be 11 digits")
#             new = input("Enter your phone number again: ")
#             customer[3] = new  # Replace the incorrect phone number

#         print(customer)

#         customer_no = "customer" + str(i)
#         all_customer.update({customer_no:customer})
#     elif con == "end":
#         customer_no = "customer" + str(i)
#         all_customer.update({customer_no:customer})
#         break
#     i += 1

# print(all_customer)


# names = []
# for name in range(6):
#     value = input("Enter your name: ")
#     while name == 2 and len(value) > 6:
#         print("Name cannot be greater than 6 characters. Press 1 to re-enter your details or press 2 to skip")
#         options = input("enter option ")
#         if options == '1':
#             value = input("Enter your name ")
#             names.append(value)
#         elif options == '2':
#             break
#     else:
#         names.append(value)
# print(names)

"""
Assignment
Write a python program using nexted for loop for a cbt exam, you can either create an array and loop through the array for names of 
students, when the student enters his or her name, append the name to an empty dictionary, the student should be able to do cbt exam
after the exam, the student score should be append to the dictionary as values. At the end of the loop,
print the student's name with highest score and print the highest score.
Note, award the student accordingly.
NOTE: Remember to use nexted for loop""

"""