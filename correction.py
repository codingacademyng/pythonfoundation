# import random
# import time

# class Bank:
#     def __init__(self):
#         self.users = {
#             327878:["Adeola Adetunji", "ade12", 40000],
#             323464:["Obalola Yinka", "oop", 5000]
#         }

#     def home(self):
#         user_dec = input("Enter 1 to login and 2 to register")
#         if user_dec == "1":
#             self.login()
#         elif user_dec == "2":
#             self.register()

#     def register(self):
#         self.fullname = input("Enter your fullname ")
#         self.passwd = input("Enter your password ")
#         self.acct_numb = random.randint(321000, 329000)
#         self.bal = 0
#         self.users.update({self.acct_numb:[self.fullname, self.passwd, self.bal]})
#         print(f"Your registration is successful and your account number is {self.acct_numb}")
#         print("Wait a sec, you will be redirected to the login page")
#         time.sleep(3)
#         self.login()
    
#     def login(self):
#         self.acct = int(input("Enter your account number "))
#         if self.acct in self.users.keys():
#             self.passw = input("Enter your password ")
#             if self.passw == self.users[self.acct][1]:
#                 print("Login Successful")
#                 time.sleep(2)
#                 self.operations()
#             else:
#                 print('Invalid details. Try again')
#                 self.login()
#         else:
#             print("Account not found. Try again")
#             self.login()

#     def operations(self):
#         resp = input("""
#               Which of the following operations would you like to perform?:
#             1) Transfer
#             2) Check Balance
#             3) Logout
#             """)
#         if resp == "1":
#             self.transfer()
#         elif resp == "2":
#             self.checkBal()
#         elif resp == "3":
#             self.home()
#         else:
#             print("Invalid input.")
#             self.operations()
    

# bank = Bank()
# bank.home()

# import random
# list_of_colors = ["red", "blue", "green", "purple", "white", "orange"]

# def playGame():
#     count = 0
#     computer_choice = random.sample(list_of_colors, 3)
#     user_choices = []
#     amount = int(input('Enter the amount you want to stake '))
#     for i in range(3):
#         userChoice = input(f"Enter the color {i + 1} ").lower()
#         user_choices.append(userChoice)

#     for item in user_choices:
#         if item in computer_choice:
#             count += 1
#     new_amount = (count  * 2) * amount
#     print(new_amount)

# playGame()
