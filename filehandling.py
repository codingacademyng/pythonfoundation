# File Handling
# myFile = open("filename", mode='r', 'a', 'w','x', encoding='t','b')
# 'r' read only and it is the default for open function. Raise error if file does not exist
# 'a' Append new content to an existing file. Create new file with the specified name if file does not exist.
# 'w' Open file for writing. Create new file with the specified name if file does not exist
# 'x' To create new file. Raise error if file already exist
# with open("filename", mode="rt") as myFile:
# fileText = open("C:\\Users\\HP\\Desktop\\pyton xclass\\filehandling.txt", "r")
# print(fileText.read())
# fileText.close()
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
#     time.sleep(1)
# myFile.close()

# myFile = open("C:\\Users\\HP\\Desktop\\pyton xclass\\filehandling.txt", 'w')
# myFile.write("\n this is a new content to append to the old file")
# myFile.close()
# myFile = open("C:\\Users\\HP\\Desktop\\pyton xclass\\filehandling.txt", 'r')
# print(myFile.read())
# myFile.close()

# myFile = open("C:\\Users\\HP\\Desktop\\pyton xclass\\filehandling.txt", 'a')
# myFile.write("\nthis is a new content to append to the old file")

# myFile = open("infile.txt", 'rt')
# print(myFile.read())
# myFile.close()
# myFile =open("/Users/mac/Documents/learning.txt", "r")
# using with open function
# with open("C:\\Users\\HP\\Desktop\\pyton xclass\\filehandling.txt", "a") as myFile:
#     myFile.write("\nthis is a new content to append to the old file")
    # print(myFile.read())

# import os
# if os.path.exists("C:\\Users\\HP\\Desktop\\pyton xclass\\filehandling.txt"):
# 	with open("C:\\Users\\HP\\Desktop\\pyton xclass\\filehandling.txt", mode="r") as myFile:
# 		# myFile.write("\nAppending a new content to it")
# 		print(myFile.read())
# else:
# 	print("file does not exits")

# if os.path.exists("/Users/mac/Desktop/learning.txt"):
#     os.remove("/Users/mac/Desktop/learning.txt")
#     print("file deleted successfully")
# else:
#     print("file not available.")
import os
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
# print(os.path.dirname(os.path.abspath("filehandling.txt")))

#ERROR HANDLING

# for i in range(3):
#     val1 = int(input('Enter numb 1 '))
#     val2 = int(input('Enter numb 2 '))
#     print(val1 + val2)

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


# try:
#     var1 = int(input("Enter the first value "))
#     var2 = int(input("Enter the second value "))
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
#         a = input("enter quotient value ")
#         b =input("enter divisor value ")
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

# inp = input("Enter your name ")
# if inp == "Ade":
#     raise ValueError("I don't like you")

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


# Python Regular Expression
import re

# string = "Abcd 4 digits 7862 helicopter 30"
# string =input("Enter the word you want to find: ") #this will find only the word "helicopeter"
# pattern= r'[0-9]' #this will find all digits in string but it will be finding it singly
# pattern= r'[0-9]+' #this will find all digits in string but it will be finding it as written in string
# pattern= r'[a-zA-Z]+' #this will find all alphabets in string but it will be finding it as written in string
# pattern = r'[a-zA-Z0-9]+'
# # # pattern = r'[a-zA-Z]+'
# match = re.findall(pattern, string)
# if match:
#         print("match found")
#         print(match)
# else:
#         print("Could not find pattern")
word = """
apple
Cherries
Tomatoes
Date
Guava
"""
# pattern = r'.*s'
# pattern = r'[aeiou].+' #
# match = re.findall(pattern, word)
# print(match)
# for m in match:
#     print(m)
# else:
#     print("No match found")
import re
# email = input("Enter your email address ")
pattern = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
# look = re.search(pattern, email)
# if look:
#     print("Email match found")
# else:
#     print("Email match not found")
# nm = input("ENter your name ")
# em = input("ENter your email ")
# result = re.search(pattern, em)
# while not result:
#     print("Invalid email typeblajjj")
#     em = input("ENter your email ")
#     result = re.search(pattern, em)
# pd = input("ENter your passw ")

# import re

txt = "hello planet"

# #Search for a sequence that starts with "p", followed by four (any) characters, and a "t":

# x = re.findall("p....t", txt)
# print(x)
# import re

# txt = "hello planet plant planet"
# x = r'[a-z].+'
# match = re.search(txt, x)
# print(match)

# # #Check if the string starts with 'hello':
# x = re.findall("^hello", txt)
# if x:
#   print(x)
# else:
#   print("No match")
import re
text = """the value of a thing will determine the capacity you put to it. the value of 2019 is what you get in 2020
and now you get the value of 2020 in 2021"""


# var = "Hello world"
# res = re.sub(r"^Hello", "Hi", var)
# print(res)

# val = re.search("^the.*2021$", text)
# if val:
#     print("We have a match")
# else:
#     print("No match detected")

# re function
# findall() : returns list containing all matches
# search() : returns object of a match if there is a match anywhere in the string
# split() : returns a list where the string has been split at each match
# sub() : replace one or many matches  with a string

# re matacharacters
# [] : refers to set of characters to match eg "[a-m]"
# \ : can be use to escape special charactter eg "\d"
# . : any character except newline character eg 'he.o'
# ^ : starts with eg "^the"
# $ : ends with eg "world$"
# * : zero or more occurrences eg "aix*"
# + : one or more occurrences eg "aix+"
# {} : exactly specified number of occurrence eg "al{2}"
# | : either or eg "this|that"
# () : capture and group

# re special Sequences
# \A : returns a match if the specified characters are at the begining of the string eg "\AThe"
# \b : returns a match if the specified characters are at the begining or at the end of the string eg r"\bthe" or r"the\b"
# \B : returns a match if the specified characters are present but not at the begining or at the end of the string eg r"\Bthe" or r"the\B"
# \d : returns a match where the string contains digits (number from 0-9) eg "\d"
# \D : returns a match where the string does not contains digits eg "\D"
# \s : returns a match where the string contains a white space character eg "\s"
# \S : returns a match where the string does not contains a white space character eg "\S"
# \w : returns a match where the string contains characters from letter A-Z and digits from 0-9 and underscore eg "\w"
# \W : returns a match where the string does not contains any word characters
# \Z : returns a match if the specified characters are at the end of the string

# re sets
# [arn] : returns a match where one of the specified characters (a or r or n ) are present
# [a-n] : returns a match for any lower case character alphabetically between a and n
# [^arn] : returns a match for any character except a, r and n
# [0123] : returns a match where any of the specified digits (0, 1, 2, 3) are present
# [0-9] : returns a match for any digits between 0 and 9
# [0-5][0-9] : returns a match for any two digits between 00 and 59
# [a-zA-Z] : returns a match for any character alphabetically between a and z lower case or upper case
# [+] : returns a match for any character in the string
text = """the value of a thing will determine the capacity you put to it. the value of 2019 is what you get in 2020
and now you get the value of 2020 in 2021"""
# x = re.findall(r'you', text)
# print(x)
# x = re.search(r'you', text)
# if x:
#     print("A match found")
# print(x.group())    
# a = tuple(x.group())
# print(a)
# tx = re.sub(r'\d', '[]', text)
# print(tx)
# tx = re.sub(r'capacity', 'ability', text)
# print(tx)
# tx = re.sub(r'\d', '[]', text, 4)
# print(tx)

# import re

# a =input("Enter your phone number ")
# #Find all lower case characters alphabetically between "a" and "m":

# x = re.findall("[0-7]", a)
# if x:
# 	print("Phone number is correct")
# else:
# 	print("Invalid phone number")
# Python DataTime
import datetime
# tim = datetime.datetime.now()
# print(tim)
# print(tim.hour)
# tm = datetime.datetime(2021, 4, 10)
# print(tm)
# print(tm.month)
# tm = datetime.datetime(2021, 4, 10, 12, 30, 20)
# print(tm)
# strftime() method - use to format datetime object into readable string
# # strftime format codes
# %a : returns weekday in short version eg wed
# %A : returns weekday in full version eg wednesday
# %w : returns weekday in number version from 0-6 where 0 means sunday eg wed is 3
# %d : returns day of the month in number version from 01-31
# %b : returns month name in short version eg Dec
# %B : returns month name in full version eg December
# %m : returns month in number formart from 01-12
# %y : returns year in short version eg 2021 is 21
# %Y : returns year in full version eg 2021
# %H : returns hour in 24hrs format from 00-23
# %I : returns hour in 12hrs format from 00-12
# %p : returns AM or PM of time
# %M : returns minute of time from 00-59
# %S : returns seconds of time from 00-59
# %f : returns microseconds of time form 000000-999999
# %Z : for timezone
# %j : days number of the year from 001-366
# %U : return week number of the year from 00-52
# tm = datetime.datetime.now()
# print(tm.strftime("%p"))
# while True:
#     tm = datetime.datetime.now()
#     # print(tm)
#     if tm.strftime("%I") == "10" and tm.strftime("%M") == "15" and tm.strftime("%S") == "00" and tm.strftime("%p") == "AM":
#         print("it's time for break")
#         break
#     else:
#         print("Keep learning")
# import time
# print(time.strftime("%z"))
# import datetime

# rang =[]
rang = [rn for rn in range(0,60)]
# print(rang)
# # This code is equivalent to:
# for rn in range(0, 10):
#     rang.append(rn)
# check = int(datetime.datetime.now().strftime("%M"))
# print(check)   
# while True:
#     time =datetime.datetime.now()
#     nexttime = time.strftime('%M')
#     if int(nexttime) in rang and check == int(nexttime):
#         for i in range(5):
#             print("i am going for class today")
#     check = int(nexttime )+ 1

# hour = hour[0]+str(int(hour[1]) + 2)

# Python Math class
# import math
# l = [2, 4, 5, 7, 3]
# print(min(l))
# print(max(l))
# print(abs(-5.34))
# print(pow(5, 3))
# print(math.sqrt(9))
# print(math.ceil(6.3492))
# print(math.floor(5.6732))
# print(math.pi)
# print(math.pi * 1000 + 25)