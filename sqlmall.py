#ASSIGNMENT: Create a shopping mall app: It should have 3 categories: Food, Drinks,Clothings. Each of the categories should have their respective product names, price and quanity.
#APP DETAILS: 
# 1) Login and Register page for customers
# 2) A shopping page where user would be able to pick any products available in the mall and pay for it. The price of the product should be bsed on the quantity selected and the product's quantity should reduce after each purchase. Save the transaction in the sales table

import mysql.connector as connection

mycon = connection.connect(host='127.0.0.1', user='root', passwd='ayilara10maranatha30' , database='sqlmall')
cursor = mycon.cursor()
# cursor.execute("CREATE DATABASE sqlmall")
# cursor.execute("CREATE TABLE clothings (Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(30), Price INT, Quantity INT)")
# cursor.execute("CREATE TABLE customers (customer_id INT PRIMARY KEY, username VARCHAR (20), password VARCHAR(30))")
# cursor.execute("CREATE TABLE sales (sales_id INT PRIMARY KEY AUTO_INCREMENT, customer_id INT, product_name VARCHAR(50), product_quant INT, total_amount INT)")

import random
import time
def home():
    inp = input("1 reg, 2 log ")
    if inp == "1":
        reg()
    elif inp == "2":
        log()

def reg():
    uname = input('username ')
    pwd = input('passw ')
    c_id = random.randrange(212000, 212900)
    query = "INSERT INTO customers (customer_id, username, password) VALUES(%s, %s, %s)"
    val = (c_id, uname, pwd)
    cursor.execute(query, val)
    mycon.commit()
    print(f"Dear {uname}, your reg is comp and your id is {c_id}")
    time.sleep(2)
    log()

def log():
    global id
    id = int(input("Enter id "))
    pwd = input('passw ')
    query = "SELECT * FROM customers WHERE customer_id = %s and password = %s"
    val = (id, pwd)
    cursor.execute(query, val)
    res = cursor.fetchone()
    if res:
        print("succes")
        start()
        time.sleep(2)
    else:
        print("invalid")
        print(res)
        log()

def start():
    print('Welcome to the mall. Which of the following categories would you like to shop in? ')
    categories = ["drinks", "food", "clothings"]
    print(categories)
    user_resp = input(">>> ").lower()
    if user_resp in categories:
        query = f"SELECT Name FROM {user_resp}"
        cursor.execute(query)
        products = cursor.fetchall()
        print(f"{products} are the products we have in this category.")
        decision = input('Which one would you like o purchae? ').lower()
        while (decision,) not in products:
            print('Select from the available products')
            decision = input('Which one would you like o purchae? ').lower()
        else:
            pquery = f"SELECT * FROM {user_resp} WHERE Name = {'%s'}"
            val = (decision,)
            cursor.execute(pquery, val)
            items = cursor.fetchone()
            print(f"Product Name: {items[1]}")
            print(f"Product Price: {items[2]}")
            print(f"Product Quantiy: {items[3]}")
            am_pur = int(input('Enter the quantity you want to purchase '))
            while am_pur > items[3]:
                print("Quantity above stock")
                am_pur = int('Enter the quantity you want to purchase ')
            else:
                total_price = am_pur * items[2]
                print(f"Your total amount is {total_price}")
                new_quan = items[3] - am_pur
                uquery = f"UPDATE {user_resp} SET Quantity = {'%s'} WHERE Name = {'%s'}"
                val = (new_quan, decision)
                cursor.execute(uquery, val)
                mycon.commit()
                squery = "INSERT INTO sales (customer_id, product_name, product_quant, total_amount) VALUES(%s, %s, %s, %s)"
                val = (id, decision, am_pur, total_price)
                cursor.execute(squery, val)
                mycon.commit()
                time.sleep(3)
                print("Your purchase is successfull")
                quest = input('Enter 1 to shop again and 2 to logout')
                if quest == "1":
                    start()
                else:
                    home()

    else:
        print("Category does not exist. Try again")

# home()

#ASSIGNMENT: Modify this code. Add an admin table to the database. The admin should be able to add products to the products table