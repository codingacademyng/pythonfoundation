
# ASSIGNMENT: Create a python program that would ask for the user's name and phone number. Determine the network the user is using and inform the user.
# phone_number = input("Enter your phone number ")
# Airtel = ("0802", "0808", "0708", "0812", "0701", "0902", "0901", "0904", "0907", "0912")
# MTN = ("0803", "0806", "0703", "0706", "0813", "0816", "0810", "0814", "0903", "0906", "0913", "0916", "0705", "07026", "0704")
# GLO = ("0805", "0807", "0705", "0815", "0811", "0905", "0915")
# Etisalat =  ("0809", "0818", "0817", "0909","0908")
# if phone_number.startswith(Airtel):
#     print(f"Your network is airtel ")
# elif phone_number.startswith(MTN):
#     print(f"Your network is mtn ")
# elif phone_number.startswith(GLO):
#     print(f"Your network is glo ")
# elif phone_number.startswith(Etisalat):
#     print(f"Your network is 9 Mobile ")
# else:
#     print("Invalid phone number.")

#TEST QUESTION 
# def outer_func(y):
#     x = 2
#     def inner_func():
#         return x + y
#     x = x + 2
#     y = 2
#     return inner_func
# results = outer_func(9)
# print(results())



#ASSIGNMENT1: Create a python program that would ask the user to supply a word. Determine whether the word is a palindrome or not. If it is, inform the user and add it to an empty list you've created and if it isn't, inform the user.
#ASSIGNMENT2: Create a python program that would ask the user to write an article. Afterwards ask the user if the user would wish to replace a word in the article. If so, ask for the word they want to replace and what they would love to replace it with and if not print the original article the user wrote.
# user_word = input("Enter your word ")

# new_userword = user_word.replace(" ", "")
# print(new_userword)

# user_article = input("Enter your article ")
# user_choice = input("Do you wish to replace a word? ").lower()
# if user_choice == "yes":
#     old_word = input("Enter the word you wish to replace ")
#     new_word = input("Enter the new word ")
#     new_article = user_article.replace(old_word, new_word)
#     print(new_article)
# else:
#     print(user_article)


# phone_book = {"Tunji":"09012345678", "Seyi":"0802345672", "Caroline":"08123567812"}
# user_inp = input("Welcome to Nath's phonebook. Which of the following operations would you like to perform\n1) Adding to your phonebook\n2) Viewing your phonebook\n3) Deleting from your phonebook\n")

# if user_inp == "1":
#     cName = input("Enter new contact's name ")
#     cNum = input("ENter new contact's number ")
#     phone_book.update({cName:cNum})
#     print(phone_book)
# elif user_inp == "2":
#     print(phone_book)
# elif user_inp == "3":
#     delName = input("ENter the name of the contact you want to delete ")
#     if delName in phone_book:
#         del phone_book[delName]
#         print(phone_book)
#     else:
#         print("Contact does not exist")
# import time
# questions = ["How many states are in Nigeria", "Who is your instructor"]
# options = ["a. 35\nb. 36", "a. Nath\nb. Maranatha"]
# answers = ["b", "b"]
# exam_users = {}

# for i in range(2):
#     username = input("Enter your username ")
#     score = 0
#     for que in questions:
#         print(que)
#         index = questions.index(que)
#         print(options[index])
#         correct_answer = answers[index]
#         user_ans = input("Enter your answer ").lower()
#         if user_ans == correct_answer:
#             score += 10
#     exam_users.update({username:score})
#     print("Exam is over.")
#     time.sleep(2)

# print(exam_users)
# highest_student = max(exam_users, key=exam_users.get)
# highest_score = max(exam_users.values())


#Write a Python program to validate a user's input of a numerical value. If the input is not a number, provide feedback; otherwise, determine if it's even or odd.
# try:
#     num = int(input("Enter a number "))
#     if num % 2 == 0:
#         print('This is an even number')
#     else:
#         print("This is an odd number")
# except ValueError:
#     print("The input supplied must be a numerical value")


# Write a for loop that finds and prints all prime numbers from 1 to 50. convert the for loop-based prime number computation into a list comprehension.
# prime_nums = []
# for x in range(1, 50):
#     for y in range(2, x):
#         if x % y == 0:
#             break
#     else:
#         prime_nums.append(x)
# # LIST COMPREHENSION METHOD
# prime_nums = [x for x in range(1, 50) if all (x % j != 0 for j in range(2, x))]
# print(prime_nums)


# Write a function called square_odd that has one parameter. Your function must calculate the square of each odd number in a list.Return a Python list containing the squared values. Challenge yourself: Solve this problem with a list comprehension!
# def square_odd(arr):
#     if type(arr) == list:
#         new_arr = [num * num for num in arr if num % 2 != 0]
#         print(new_arr)
#     else:
#         print("Function only takes in array type objects")


# Write a Python program that accepts three sides of a triangle and checks if it's an equlateral, isosceless or scalene triangle.
#Note: equilateral triangle - has 3 equal sides, isosceles triangle- has at least 2 equal sides. scalene triangle - has 3 unequal sides.
# user_inp = []
# first_ang = int(input("Enter angle 1 "))
# second_ang = int(input("Enter angle 2 "))
# third_ang = int(input("Enter angle 3 "))
# angle_match = 0
# for i in user_inp:
#     if user_inp.count(i) > 1:
#         angle_match += 1
# if angle_match == 3:
#     print("Equil")
# elif angle_match == 2:
#     print("isos")
# else:
#     print("scalene")
# # REVISED METHOD
# user_inp = []
# for i in range(3):
#     angle = int(input(f"Enter angle {i + 1} "))
#     user_inp.append(angle)
# angle_arr = [1 for i in user_inp if user_inp.count(i) > 1]
# if sum(angle_arr) == 3:
#     print("Equil")
# elif sum(angle_arr) == 2:
#     print("isos")
# else:
#     print("scalene")

# Given the list of dictionaries below where each dictionary represents a property, use a loop to add price per area to each dictionary: price_per_m2.
# properties = [{'price_in_usd': 68663.03, 'area_in_m2': 208, 'room_num': 3}, {'price_in_usd': 100412.94, 'area_in_m2': 256, 'room_num': 4}, {'price_in_usd': 41967.85, 'area_in_m2': 87, 'room_num': 4}, {'price_in_usd': 80186.97, 'area_in_m2': 158, 'room_num': 2}, {'price_in_usd': 48405.36, 'area_in_m2': 249, 'room_num': 3}]

# for prpty in properties:
#     price_per_m2 = prpty.get("price_in_usd") / prpty.get("area_in_m2")
#     prpty.update({"price_per_m2":round(price_per_m2, 2)})
# print(properties)



# Exceeding the prescribed speed limit results in a penalty. The fine amount is calculated by multiplying the excess speed in km/h by 5,with a maximum fine capped at #194,750. Write a python program that (1) prompt a user for the name,speed limit and actual speed. (2) calculate the fine according to the rules above.
# (3) Output the name and the size of the fine on the screen.
# name = input("Enter your name ")
# speed_limit = int(input("Enter your speed in km/h "))
# actual_spd = int(input("Enter your actual speed "))
# if actual_spd > speed_limit:
#   excess_sp = actual_spd - speed_limit

#   user_fine = min(excess_sp * 5, 194750)

#   print(f"Dear {name}, you have exceeded the speed limit and your fine is {user_fine}")