# Python Database (Mysql)
# To download mysql connector user: pip install mysql-connector
import mysql.connector as connection
mycon = connection.connect(host='127.0.0.1', user='root', passwd='ayilara10maranatha30' , database='pythonsql')
mycursor = mycon.cursor()

# mycursor.execute("CREATE DATABASE pythonsql")
# mycursor.execute("DROP DATABASE pythonsql")
# mycursor.execute("SHOW DATABASES")

# for db in mycursor:
#     print(db)

# mycursor.execute("CREATE TABLE customers (ctm_id INT, Ful_Name VARCHAR(20), Address VARCHAR(50), Phone VARCHAR(11), Password VARCHAR(20))")
# mycursor.execute("SHOW TABLES")
# for table in mycursor: 
#     print(table)

# mycursor.execute("ALTER TABLE customers CHANGE ctm_id ctm_id INT PRIMARY KEY AUTO_INCREMENT")
# mycursor.execute("ALTER TABLE customers ADD UNIQUE(Phone)")


# myquery = "INSERT INTO customers (Ful_Name, Address, Phone, Password) VALUES(%s, %s, %s, %s)"
# val = ("Seyioola", "Paris", "08032345672", "francoe")
# mycursor.execute(myquery, val)
# mycon.commit()
# print(mycursor.rowcount, 'record updated successfuly')

# myquery = "INSERT INTO customers (Ful_Name, Address, Phone, Password) VALUES(%s, %s, %s, %s)"
# fullname = input('enter your fullname: ') 
# address = input('enter your address: ')
# phone_number = input('enter your phone_number: ')
# password = input('enter your password: ')
# val = (fullname, address, phone_number, password)
# mycursor.execute(myquery, val)
# mycon.commit()

# for i in range(3):
#     myquery = "INSERT INTO customers (Ful_Name, Address, Phone, Password) VALUES(%s, %s, %s, %s)"
#     fullname = input('enter your fullname: ') 
#     address = input('enter your address: ')
#     phone_number = input('enter your phone_number: ')
#     password = input('enter your password: ')
#     val = (fullname, address, phone_number, password)
#     mycursor.execute(myquery, val)
#     mycon.commit()

# query = "SELECT * FROM customers"
# mycursor.execute(query)
# output = mycursor.fetchall()
# print(output)

# for inf in output:
#   print(inf)

# mmm = "SELECT * FROM customers where ctm_id = %s"
# val = (2,)
# mycursor.execute(mmm, val)
# nm = mycursor.fetchone()
# print(nm)
# mmm = "SELECT * FROM customers where Address = %s"
# val = ("Paris",)
# mycursor.execute(mmm, val)
# nm = mycursor.fetchall()
# print(nm)

# user_id = [1, 23, 40, 56]
# for i in user_id:
#     mmm = "SELECT Address FROM customers where ctm_id = %s"
#     val = (i,)
#     mycursor.execute(mmm, val)
#     nm = mycursor.fetchone()
#     print(nm)

# username = input("Enter your username ")
# password = input("Enter your passord ")

# myquery = "SELECT * FROM customers where Ful_name =%s and Password = %s"
# val = (username, password)
# mycursor.execute(myquery, val)
# output = mycursor.fetchone()

# if output:
#     print("LLogin successful")
#     print(output)
# else:
#     print("Print invalid details")
#     print(output)

# query = "SELECT Ful_Name, Phone FROM customers"
# query = "SELECT * FROM customers ORDER BY ful_Name DESC"
# val = ('09013140700', val)

# phone = input("Enter your phone number ")
# pin = input("Enter your pin ")
# query = "SELECT Ful_Name, Address FROM customers WHERE Phone=%s AND Password=%s "
# val = (phone, pin)
# mycursor.execute(query, val)
# myreg = mycursor.fetchall()
# myreg = mycursor.fetchone()
# print(myreg)
# for info in myreg:
#     print(info)
# mycon.commit()
# print(mycursor.rowcount, 'selected successfuly')
# mycon.close()

# sql = "UPDATE customers SET Address = %s where ctm_id = %s"
# val =("Maldives", 2)
# mycursor.execute(sql, val)
# mycon.commit()
# print(mycursor.rowcount, 'record updated successfuly')

# sql = "DELETE FROM customers WHERE Phone=%s"
# val =('08081306253',)
# mycursor.execute(sql, val)
# mycon.commit()
# print(mycursor.rowcount, 'record deleted successfuly')

# sql = "DROP DATABASE cbtte"
# mycursor.execute(sql)