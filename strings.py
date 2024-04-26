# STRINGS

# # Python String Class
# name = ('sunday') #they are characters and always in quote
# val = str(10)

# name3 = """My name is faith and i am very very stubborn 
# """ #is either use 'faith' or this "faith" or this """faith"""
# name4 = "faith's car"
# val = "False"
# val1 = False
# print(type(val))
# print(type(val1))
# print(val)  
# print(type(val)) 
# print('i am ' + val + 'years old')
junaid = ['s', 'u', 'n', 'd', 'a', 'y']
# name = 'Monday'
name = 'commented'
# name1 = ' c o m m e n t e d'
#         ' 0 1 2 3 4 5 6 7 8'
      #  -9  -8  -7  -6  -5  -4  -3  -2  -1
# print(name) #indexing
# print(type(name))
# print(name[2])
# print(name[4])
# print(name[:5]) #this numbers are index numbers. String can be sliced, you can request for numbers from an index to an index, this process is called slicing
# print(name[-3:])
# print(name[2:])
# print(name[1:6])
# print(name[:3])
# print(len(name))
# print(len(junaid))
 #len means length of character or value
# name2 = "shade"
# name = "234567"
# print(name[2])
# print(name[-3:])
# print(len(name))

comment = """commented that This is a python class. it was started 
last week and still continue through
this week. the number of people in this class is"""
# comment = "Definition: 'what is yor name?'"

# print(comment)
# print(len(comment))
# print(comment[27:39])
# print(comment[2:])
# print(comment[0:9])
# print(comment[-2]) 
# print(comment[-30:-5])


# String Methods
# print(comment.startswith('python'))
# print(comment.startswith('we')) #comment here is the variable name, .startswith() is python in built function while "we" is the argument we are passing i.e. the word we are trying to find out.
# comment = """commented that This is a python class. it was started 
# #           last week and still continue through
# #           this week. the number of people in this class is """
# print(comment.endswith("is"))
# print("the length of comment is ", len(comment))

comment = """    commented that This is a python class. it was started 
last week and still continue through
this week. the number of people in this class is    """
# .strip()
# # # Strip() function
# print('length before strip is ', len(comment))
# print('length after strip is ', len(comment.strip()))

# val = input("Enter name ").strip()
# val2 = input("Enter name ").strip()
# if val == "*":
#    print(val)
# else:
#    print(val2)
# val1 = float(input("enter value 1 "))
# val2 = float(input("enter value 2 "))
# name = 'Register User'
# print('''
#               addition
#               subtraction
# '''
# )


# add = val1 + val2
# print(add)




# val1 = float(input("enter value 1 "))
# val2 = float(input("enter value 2 "))
# name = "addition"
# oper = input('enter operation: ')
# if oper.strip() == name:
#     print(val1 + val2)

# else:
#     print('Error')

# print("""
#       subtraction
#       addition
      
#       """)


# if oper == '   addition':
#   print(val1 + val2)
# elif oper.strip() == 'subtraction'.strip():
#   print(val1 - val2)
# else:
#   print('invalid selection')
# print(len(value))
# print(len(value.strip()))

# Lower() function
# name = 'SUNDAY'
# print(name.lower()) # .lower() is used to transform all inputs by user to lowercase
# value = "login" #while using .lower(), your condition must be written in lowercase
# user = input("please enter login to continue: ").lower()
# if value == user:
#   print('welcome')
# else: 
#     print("invalid input")

# Upper() function
# value = "LOGIN"
# # print(value.upper())
# user = input("please enter method to continue ").upper()
# if value == user:
#   print('welcome')
# else: 
#     print("invalid input")

# # Replace() function
comment = """  commented that This is a python class. it was started 
          last week and still continue through
          this week. the number of people in this class is   """
name = "sunday"
num = 16

# comment = f"""{name} commented that This is a python class. it was started and last week and still continue through
#   this week. the number of people in this class is {num}"""
# print(comment)
# comment = 'This is \n a comment'
# print(comment)
# newval = comment.replace("people", "students")
# print(newval)


# Split() function
# print(comment.split())
# print(comment.split('.'))
# name = comment.replace('This', 'this')
# print(name)
print(comment.split('week'))


"""
Write an algorithm that will ask a user to write an article, ask if the user will like to change any word
replace a word from the article with a new word, print both the old article and the new article
"""