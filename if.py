# taofeeq_phnbk = {"landlord's-daughter":"0801253278", "babe4":"09025436785", "main-gf":"0812356409"}

# user_inp = input('Welcome to your phonebook. WHich of the following operations would you like to perform:\n1) Viewing the phonebook\n2)Adding to the phonebook\n3)Deleting from your phonebook ')
# if user_inp == "1":
#     print(taofeeq_phnbk)
# elif user_inp == "2":
#     cname = input('Enter your new contact"s name ')
#     number = input('Enter your new contact"s number ')
#     taofeeq_phnbk.update({cname:number})
#     print(taofeeq_phnbk)
# elif user_inp == "3":
#     cname = input("Enter the contact name you'd like to remove ")
#     if cname in taofeeq_phnbk:
#         taofeeq_phnbk.pop(cname)
#         print(taofeeq_phnbk)
#     else:
#         print('Contact not found')
# else:
#     print("Invalid input")

#IF AND ELSE STATEMENT
# IF statement  is the  block of code that would run if a particular condition evaluates to True
# x = 10
# if x < 3:
#     print("X is less than 3")
#     print("Hello")
# else:
#     print("x is greater than or equal to 3")

# score1 = input('Enter your first score: ')
# score2 = input('Enter your second score: ')
# total_score = float(score1) + float(score2)
# if total_score <= 10:
#     print("You score below cutoff score")
# elif total_score > 20:
#     print("You performed excellently")
# else:
#     print("Your score is okay")


# name = "shadee"

# if name == "bode":
#     print("Name is bode")
# elif name == "shade":
#     print("Name is shade")
# elif name == "ade":
#     print("Name is ade")
# else:
#     print("None of the above")


# # how to use multiple operator with if statement
# name = input("Enter your name ").strip().lower()
# if name == "ade":
#     print("Ade can come in")
# else:
#     print("Ade is not here")
# food = input('What food is available: ').strip().lower()
# protein = input('What meat is available ').strip().lower()
# meats = ('fish', 'egg', 'ponmo')
# # meat = 'fish'
# foods = ["rice", "beans", "semo"]
# if food in foods and protein in meats:
#     # print(f"i will buy {food} and {protein}")
#     print("I will buy " + food + " and " + protein)
# else:
#     print('I will not buy anything')

# menu = input('What food is available: ')
# protein = input('What meat is available ')
# options = ('fish', 'egg', 'ponmo')

# if (menu =='rice' and (protein == 'fish'  or protein == 'beef')):
#     print('I will buy rice')
# else:
#     print('I will not buy anything')
# menu = "rice"
# meat = "egg"
# men = "rice"  # check this
# meats = "egg"
# if menu is men and meat is meats:
#     print("meat is available")
# else:
#     print("i will not buy anything")

a = "Ade"
b = "Ola"
c = "Ade"
d = "Ola"

# if a == c:
#     print("This is true")
#     if b == a:
#         print("Yes")
#     else:
#         print('One')
# else:
#     print("Nope")
# name = "ade"
# if name == "de":
#     print("yes")
# print("Goodbye")

# if a == c:
#     if b == d:
#         if "a" == "a":
#             print("Hello")
#         print("A and C are similar, likewise b and d are also similar")
#     else:
#         print("Only A and C are similar")
# else:
#     print("I can't evaluate the next block of code because the first one is not true")



registration_status = input('Are you a student of SQI by registration? ')
if registration_status.lower() == 'yes':
    user = input('enter your gender ')
    if user.lower() == 'male':
        option = input('Enter your course ')
        if option.lower() == 'datascience':
            print('you are welcome to class')
        else:
            print('go to the frontdesk')
    elif user.lower() == 'female':
        us = input('what are you here for? ')
        if us.lower() == 'web development':
            print('go to the next class')
        else:
            print('your course is not here')
    elif user.lower() == 'bobrisky gender':
        de = input('what is your business here ')
        if de == 'data analysis':
            print('you are good to go to michael"s class')
        else:
            print('###')
    else:
        print("you are not supposed to be here. We don't accept aliens")
else:
    print('Go back home')

# x = 10
# if x == 10:
#     print("hello")
#     if x == 10:
#         print("Hi")

# student_confirmation = input("Are you a student of SQI ").lower()
# if student_confirmation == "yes":
#     print("Okay, you are welcome to schoool")
#     fee = input("Have you paid your fee? ").lower()
#     if fee == "yes":
#         course = input("Please enter your course ").lower()
#         if course == "data science":
#             level = input("What level are you ")
#             if level == "2":
#                 print("You are currently running python core and ipytho")
#             elif level == "3":
#                 print("You are currently running Django and Numpy")
#             elif level == "4":
#                 print("You are currently running Pandas and Webscrapping")
#             elif level == "5":
#                 print("You are currently running Machine Learning")
#             else:
#                 print("Your level is not here, go to the frontdesk")
#                 enrol = input("Do you want to enroll for  a new level? ")
#                 if enrol == "yes":
#                     print("please pay to sqi account")
#                 else:
#                     print("Please go back home")
#         else:
#             print("Your course is not here, go to the frontdesk")
#     elif fee == "no":
#         payment = input("Do you want to pay now? ")
#         if payment == "yes":
#             print("please pay to sqi account")
#         else:
#             print("Ma lo ile yin")
#     else:
#         print("You need to pay or go back home")
# elif student_confirmation == "no":
#     register = input("Do you want to register ")
#     if register == "yes":
#         course = input("Which course would you like to register for? ")
#         courses = [
#             "datascience",
#             "graphic design",
#             "software engineering",
#             "product design"
#         ]
#         if course in courses:
#             print(f"we offer {course}")
#         elif course not in courses:
#             print(f"we don't offer {course}")
#     elif register == "no":
#         ask = input("What are you here for ")

# else:
#     print("Go back home!")



# NESTED IFs
# SQI Student
# students_info = ['timilehin akande', 'maya marvelous', 'abbas mustapha', 'olayele gbenga', 'folashade adio']
# registration_no = ['220708', '220709', '220710', '220711', '220712']
# course_allow = ('data science')
# students_name = input('Enter your name: ')
# if students_name.lower() in students_info:
#     registration = input('Enter your registration number: ')
#     if registration in registration_no:
#         course = input("Enter your course: ")
#         if course.lower() == course_allow:
#             print('You are welcome to class')
#         else:
#             print("This is not your class")
#     else:
#         print("Pls go to the frontdesk")
# else:
#     print('Go to the frontdesk to sort yourself')

# drinks = input("Which Drink do you have? ").lower()
# if drinks == "fanta":
#     print("I will buy Fanta")
#     condition = input("Is the fanta cold? ")
#     if condition == "yes":
#         print("Give me cold fanta")
#     elif condition == "not too cold":
#         print("I will manage the drink")
#     elif condition =="No":
#         print("It is a hot weather, i won't be able to drink hot drink")
#     else:
#         print("I don't like your drink")
# elif drinks == "coke":
#     bottle = input("Is it can or plastic? ").capitalize()
#     if bottle == "Plastic":
#         coldness = input("Is your coke cold? ")
#         if coldness == "yes":
#             print("Give me cold coke")
#         else:
#             print("I won't buy any drink")
#     elif bottle == "Can":
#         cond = input("Did you buy them this month? ")
#         if cond == "yes":
#             print("Pls give me can coke")
#         else:
#             print("I can't buy expired drink")
# elif drinks == "Sprite":
#     print("I will buy Sprite")
# elif drinks == "malt":
#     print("I will buy Malt")
# else:
#     print("I will not buy any drink")

# import time
# print("Student: Good afternoon Sir; \n Instructor: Good Afternoon?")
# time.sleep(2)
# instruction1 = input("Are you a student of this school? ").lower()
# if instruction1 == "yes":
#     time.sleep(2)
#     department= input("Which course are you studying? ").lower()
#     if department == 'data science':
#         print("You are welcome to class")
#     else:
#         print('This is not your class, kindly go to the frontdesk')

# elif instruction1 == "no":
#     registration = input("Do you want to register? ").lower()

#     if registration == "yes":
#         time_of_registration = input("When do you want to register? ").lower()

#         if time_of_registration == "now":
#             print("Go to the frontdesk to register")

#         elif time_of_registration == "later":
#             print("Come back later to register")
#         elif time_of_registration == "no":
#             print("You are not allowed to be here")
#         else:
#             print("Go back home")
#     elif registration == "no":
#         reason = input("Then, what are you here for? ").lower()
#         if reason == "enquiry":
#             print("Go to the front Desk to enquire")
#         else:
#             print("Excuse us, we are having a class")

# else:
#     print("We don't accommodate visitors")
# num = int(input("Enter any number "))
# if num > 10:
#     print("Your number is greater than 10")
# elif num < 10:
#     print("Your number is less than 10")
# elif num == 10:
#     print("Your number is equals to 10")


# name1 = {
#     3012345:["ade", "1234", 0],
#     310222:["bola", "bola12", 3]
# }
# login = [3012345, 310222]
# pwd = ["1234", "bola12"]

# login_id = int(input("Enter your login id "))
# passwd = input("Enter your password ")

# if login_id in login:
#     login_id_index = login.index(login_id)
#     if pwd[login_id_index] == passwd:
#         print("login successful")

# if login_id in name1:
#     if name1.get(login_id)[1] == passwd:
#         print("Login successful")



# ASSIGNMENT: Create a ussd complier that would active after dialing *321#