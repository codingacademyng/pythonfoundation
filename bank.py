import random
import time
user_info = {
    32136882:["Bukunmi", "Adeola", "bk123", 5000], 
    32136135:["Shewa", "Adeniyi", "shew90", 200000], 
    32134809: ["Sodeeq", "Money", "sosotakemypain", 10000000000000000]}

def homePage():
    user_decision = input("You are welcome to Natha bank. Which of the following operation would you like to perform?:\n1. Login \n2.Register \n3. Deposit\nEnter any other key to quit\n")
    if user_decision == "1":
        login()
    elif user_decision == "2":
        register()
    elif user_decision == "3":
        deposit()

def register():
    fName = input("Enter your first name ")
    LName = input("Enter your last name ")
    passw = input("Enter your password ")
    confirmpass = input("Confirm your password ")
    while passw != confirmpass:
        print("Password does not match")
        passw = input("Enter your password ")
        confirmpass = input("Confirm your password ")
    acct_num = random.randrange(32134569, 32139000)
    print(f"{fName} {LName} your registration is successful and your account number is {acct_num}")
    user_info.update({acct_num:[fName, LName, passw, 0]})
    time.sleep(1)
    login()

def login():
    global user_acct
    user_acct = int(input("Enter your account number "))
    if user_acct in user_info.keys():
        user_pass = input("Enter your password ")
        if user_pass == user_info[user_acct][2]:
            print("Login Successful")
            time.sleep(1)
            operation()
        else:
            print("Invalid Password. Try again")
            login()
    else:
        decision = input("Account not found. Enter 1 to try again, 2 to register and any other key to go home ")
        if decision == "1":
            login()
        elif decision == "2":
            register()
        else:
            homePage()

def operation():
    decision = input("Which of the following operations would you like to perform?\n1. Check Balance\n2. Transfer \n3. Logout\n")
    if decision == "1":
        checkBal()
    elif decision == "2":
        transfer()
    else:
        homePage()

def checkBal():
    print(f"Dear {user_info[user_acct][0]}, your account balance is {user_info[user_acct][3]}")
    time.sleep(2)
    operation()

def transfer():
    user_bal = user_info[user_acct][3]
    recp_acct = int(input("Enter recipient's account number "))
    if recp_acct == user_acct:
        print("You can't transfer money to yourself, Thief")
        transfer()

    elif recp_acct in user_info.keys():
        print(f"You are about to transfer to {user_info[recp_acct][0]} {user_info[recp_acct][1]}")
        amount = int(input("Enter the amount you want to transfer "))
        while amount > user_bal:
            print(f"You don't have sufficient balance. Enter amount that is lower or equal to your balance: {user_bal}")
            amount = int(input("Enter the amount you want to transfer "))
        else:
            new_am = user_bal - amount
            user_info[user_acct][3] = new_am
            recp_bal = user_info[recp_acct][3] + amount
            user_info[recp_acct][3] = recp_bal
            print("Transfer successful")
            try_again = input("Enter 1 to try again and any other key to go home ")
            if transfer == "1":
                transfer()
            else:
                operation()
    else:
        print("Account not found. Try again")
        transfer()
homePage()
