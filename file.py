# File Handling
# myFile = open("filename", mode='r', 'a', 'w','x', encoding='t','b')
# 'r' read only and it is the default for open function. Raise error if file does not exist
# 'a' Append new content to an existing file. Create new file with the specified name if file does not exist.
# 'w' Open file for writing. Create new file with the specified name if file does not exist
# 'x' To create new file. Raise error if file already exist
# with open("filename", mode="rt") as myFile:
# myfile=open("C:\\Users\\HP\\Desktop\\pyton xclass\\filehandling.txt", 'r')
# print(myfile.read())
# myfile.close()
# myFile = open("C:\\Users\\HP\\Desktop\\pyton xclass\\filehandling.txt", 'w')
# myFile.write("Hey bro. I am overriding you")
# myFile.close()
# print(myFile.read())
# myFile.write("Hello, world\n This is python class\n we are learning filehandling")
# print(myFile.read())
# myFile.close()
# myfile = open("C:\\Users\\HP\\Desktop\\pyton xclass\\filehandling.txt", 'a')
# myfile.write("Please try to listen to my words")
# myfile.close()
# print("What would you like to do? 1, Read news")
# decision= input(">>>  ")
# if decision =="1":
#     myfile = open("C:\\Users\\HP\\Desktop\\pyton xclass\\filehandling.txt", 'r')
#     print(myfile.read())
# else:
#     print("No news available")
myFile = open("C:\\Users\\HP\\Desktop\\pyton xclass\\filehandling.txt", 'r')
# print(myfile.read())
# print(myFile.read())
# print(myFile.read(21))
# print(myFile.readline())
# print(myFile.readline())
# print(myFile.readline())
# for i in range(3):
#     print(myFile.readline())
# import time
# for fouad in myFile:
#     print(fouad)
#     info= input("Enter your info: ")
#     # time.sleep(1)
# myFile.close()

# myFile = open("infile3.txt", 'w')
# myFile.write("\n this is a new content to append to the old file")
# myFile.close()
# myFile = open("infile3.txt", 'r')
# print(myFile.read())
# myFile.close()

# myFile = open("infile3.txt", 'a')
# myFile.write("\nthis is a new content to append to the old file")

# myFile = open("infile.txt", 'rt')
# print(myFile.read())
myFile.close()
# myFile =open("/Users/mac/Documents/learning.txt", "r")
# using with open function
# with open("C:\\Users\\HP\\Desktop\\pyton xclass\\filehandling.txt", "r") as myFile:
#     # myFile.write("\nthis is a new content to append to the old file")
#     print(myFile.read())

# import os
# if os.path.exists("C:\\Users\\HP\\Desktop\\pyton xclass\\filehandling.txt"):
# 	with open("C:\\Users\\HP\\Desktop\\pyton xclass\\filehandling.txt", mode="a") as myFile:
# 		myFile.write("\nAppending a new content to it")
# 		# print(myFile.read())
# else:
# 	print("file does not exits")

# if os.path.exists("/Users/mac/Desktop/learning.txt"):
#     os.remove("/Users/mac/Desktop/learning.txt")
#     print("file deleted successfully")
# else:
#     print("file not available.")
# import os
# os.mkdir("Michaal.txt")
# os.rmdir("Michaal")

# DON'T RUN!!!
# code to remove folder containing contents in it
# for root, dirs, files in os.walk("Documents"):
#     for file in files:
#     	os.remove("Documents\\"+file)
# os.rmdir("Documents")

# code to get username of any system(pc)
# import os.path
# homedir = os.path.expanduser("~")
# print(homedir)
# code to get system environment
# import os
# homedir = os.environ["PATH"]
# print(homedir)

# code to get the path of a file on your device
# # print(os.path.dirname(os.path.abspath("infile.txt")))

#ERROR HANDLING

# for i in range(3):
#    try:
#         val1 = int(input("Enter first value: "))
#         val2 = int(input("Enter second value: "))
#         print(val1 / val2)
#    except:
#         print("There is an error")
#    else:
#        print('There is no error')
#    finally:
#        print("I will always runj")


# var1 = int(input("Enter the first value "))
# var2 = int(input("Enter the second value "))
# try:
#     print(var1/var2)
# except:
#     print("Error")
# print("Hello, world!")
# Python Error Handling
# Two types of error in programming:
# compile time error and run time error
# try and except, finally

# def simpleCal():
#      for i in range(2):
#         global a, b
#         a = input("enter quotient value")
#         b =input("enter divisor value")
#         trying()
# 		# print(a/b)
		
# def trying():
#     try:
#         print(int(a)/int(b))
#     except:
#         print("We ran to a bug")
#     else:
#         print("No error occurred")
#         print(3*2)
#     finally:
#         print(4-2)
			
# simpleCal()

# def cal():
#     for i in range(4):
#         a = int(input("enter quotient value "))
#         b = int(input("enter divisor value "))
#         try:
#             print(a/b)
#         except:
#             print("divisor can not be zero")
#         else:
#             print("Calculation done successfully")
# cal()

# def cal():
#     for i in range(5):
#         a = (input("enter quotient value "))
#         b = (input("enter divisor value "))
        
#         try:
#             print(int(a)/int(b))
#         except ZeroDivisionError:
#             print("divisor can not be zero")
#         except ValueError:
#             print("value error")
#         except TypeError:
#             print("type error")
#         else: # execute if no error was raised
#             print("no error was raised")
#         finally: # execute either there is error or not
#             print("the execution was successful")
# cal()
# def num_stats(x):
#     if type(x) is not int:
#         raise TypeError('Work with Numbers Only')
#     if x == 0:
#         raise ValueError('Work with Positive Numbers Only')

#     print(f'{x} square is {x * x}')
# num_stats(x=int(input("Enter a number ")))
# a = int(input("enter quotient value"))
# b = input("enter divisor value")
# if type(b) is not int:
#     raise TypeError("divisor must be an integer type")
# else:
#     print(a/b)
# ASSIGNMENT: Create a cbt exam using python and mysql. The user's result should be stored on the database. Ensure that a user cannot retake the exam after doing it once. IF the user scores above 60, print out an admission letter for the user, else print out the rejection letter.