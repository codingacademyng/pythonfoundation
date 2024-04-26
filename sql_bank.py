import mysql.connector as connection

mycon = connection.connect(host='127.0.0.1', user='root', passwd='ayilara10maranatha30' , database='sql_bank')
mycursor = mycon.cursor()

# query = "CREATE DATABASE sql_bank"
# mycursor.execute(query)

# query = "CREATE TABLE polaris (ctm_id INT PRIMARY KEY AUTO_INCREMENT, full_name CHAR(30), address VARCHAR(50), phone_number VARCHAR(12), username VARCHAR(20), password VARCHAR(15), account_number VARCHAR(20), balance INT)"
# mycursor.execute(query)
# query = "ALTER TABLE kuda CHANGE ctm_id ctm_id INT NOT NULL AUTO_INCREMENT FIRST"
# mycursor.execute(query)

import random
def welcome():
    decision = input("Welcome to nath's online banking service. Which of the following bank would you like to use\n1. Kuda\n2. Polaris\n")
    if decision == "1":
        kuda()
    elif decision == "2":
        polaris()
    else:
        print("Invalid input")

def kuda():
    decision = input("Welcome to kuda bank. Enter 1 to login and 2 to register with us ")
    if decision == "1":
        kudaLog()
    elif decision == "2":
        kudaReg()

def kudaReg():
    user_questions = ["Fullname", "Address", "Phone_Number", "Password"]
    user_info = []
    for info in user_questions:
        user_decision = input(f"Enter your {info} ")
        user_info.append(user_decision)
    username = user_info[0][0:3] + str(random.randrange(100, 999))
    user_info.append(username)
    account_number = random.randrange(32314100, 32319000)
    user_info.append(account_number)
    acct_bal = 0
    user_info.append(acct_bal)
    query = "INSERT INTO kuda (full_name, address, phone_number, password, username, account_number, balance) VALUES(%s, %s, %s, %s, %s, %s, %s)"
    val = tuple(user_info)
    mycursor.execute(query, val)
    mycon.commit()
    print(f"Your registration is successful and your username is {username} and account number is {account_number}")
    kudaLog()

def kudaLog():
    global loginusername
    global loginpassword
    loginusername = input("Enter your username ")
    loginpassword = input("Enter your password ")
    query = "SELECT * FROM kuda WHERE username = %s and password = %s"
    val = (loginusername, loginpassword)
    mycursor.execute(query, val)
    result = mycursor.fetchone()
    if result:
        print(result)
        print("Login successful")
        kudaHome()
    else:
        print("Invalid login details. Try again")
        kudaLog()

def kudaHome():
    choice = input("1 to checkbalance, 2 to deposit 3 to transfer ")
    if choice == "1":
        kudaBal()
    elif choice == "2":
        kudaDeposit()
    elif choice == "3":
        kudaTransfer()

def kudaBal():
    query = "SELECT * FROM kuda WHERE username = %s and password = %s"
    val = (loginusername, loginpassword)
    mycursor.execute(query, val)
    result = mycursor.fetchone()
    print(f"Dear {result[1]}, your account balance is {result[7]} naira")
    kudaHome()

def kudaDeposit():
    query = "SELECT * FROM kuda WHERE username = %s and password = %s"
    val = (loginusername, loginpassword)
    mycursor.execute(query, val)
    result = mycursor.fetchone()
    amount = int(input('Enter the amount you want to deposit '))
    new_bal = result[7] + amount

    query2 = "UPDATE kuda SET balance = %s WHERE username = %s"
    val = (new_bal, loginusername)
    mycursor.execute(query2, val)
    mycon.commit()
    print(f'You have successfully deposited {amount} and your new balace is {new_bal}')
    kudaHome()

def kudaTransfer():
    query = "SELECT * FROM kuda WHERE username = %s and password = %s"
    val = (loginusername, loginpassword)
    mycursor.execute(query, val)
    result = mycursor.fetchone()
    recp_acct = input('Enter recipient"s account number ')
    recp_bank = input("Enter 1 to send to kuda, 2 to transfer to polaris")
    if recp_bank == "1":
        recp_query = "SELECT * FROM kuda where account_number = %s"
        val = (recp_acct, )
        mycursor.execute(recp_query, val)
        recp_result = mycursor.fetchone()
        if recp_result:
            recp_amount = int(input("Enter the amount you want to transfer "))
            while recp_amount > result[7]:
                print("insufficent balance. Try again")
                recp_amount = int(input("Enter the amount you want to transfer "))
            else:
                recp_bal = recp_result[7] + recp_amount
                recp_query = 'UPDATE kuda SET balance = %s WHERE username = %s'
                val = (recp_bal, recp_result[4])
                mycursor.execute(recp_query, val)
                mycon.commit()
                user_bal = result[7] - recp_amount
                recp_query = 'UPDATE kuda SET balance = %s WHERE username = %s'
                val = (user_bal, result[4])
                mycursor.execute(recp_query, val)
                mycon.commit()
                print("transfer successful")
                kudaHome()
                
        else:
            print('Account not found. Try again')
            kudaTransfer()
welcome()


#ASSIGNMENT: Create a shopping mall app: It should have 3 categories: Food, Drinks,Clothings. Each of the categories should have their respective product names, price and quanity.
#APP DETAILS: 
# 1) Login and Register page for customers
# 2) A shopping page where user would be able to pick any products available in the mall and pay for it. The price of the product should be bsed on the quantity selected and the product's quantity should reduce after each purchase. Save the transaction in the sales table