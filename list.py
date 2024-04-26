# Join() function
# word_split = comment.split()
# print(word_split)
# print(" ".join(word_split))
# value = ["rice", "beans", "yam", "banana"]
# print(value)
# print(" = ".join(value))

# # Capitalize() function
# comment = """commented that This is a python class. it was started last week and still continue through
# this week. the number of people in this class is  """
          
# print(comment.capitalize())
# print(comment.capitalize())
# print(comment.title())
# paul="i am coming\n pal"
# print(paul)

# Center() function
# print(comment.center(50))   

# Count() function
# print(comment.count("a"))

# Encode() function
# print(comment.encode())

# comment = """commented that This is a python class. it was started 
#           last week and still continue through
#           this week. the number of people in this class is  """

# In Operator
# val = "week" in comment
# print(val)
# val = "a" not in comment
# print(val)

# Concatination
# name = input('Enter the name: ')
# num = int(input('Enter the number of student: '))




# comment = f"""{name} commented that This is a python class. it was started 
#           last week and still continue through
#           this week. the number of people in this class is {num}"""


# comment = f""" commented that This is a python class. it was started 
#           last week and still continue through
# #           this week. the number of people in this class is """
# yes = comment.split()
# print(yes)
# print(type(yes))
# print('Let Append')
# name = []
# firstname = ["firstname", "lastname", "age"]
# for first in firstname:             #first here will extract the values of firstname one after the other
#     names = input("Enter your " + first + " ")
#     print(names) 
#     name.append(names)
# print(name)

# chose = input('Enter the word u want to append: ')
# yes.append(chose)
# print(yes)
# print('Let Insert')
# chose_new = input('Enter the word u want to insert: ')
# chose_n = int(input('Enter the index: '))
# yes.insert(chose_n, chose_new)
# print(yes)
# print(comment)
# new = input('Enter new word: ')
# com = comment.replace('python', new)
# print(com)
# print(comment.format(name, num))
# print(comment)


# Escape character
# print('she\'s is the owner paul says and i qoute" GOD IS GOOD "')
# print('she\'s ')
# print("she's")
# print('she is the\b owner\b ')
# print('she is the\t owner')


# Array:
#     list
#     tuple
#     set
#     dictionary
# names = {"sola", "sade", "tunde", "bunmi"}
# print(names)

# List: is a collection which is ordered and changeable.
#  A list is created with a square bracket [] or list() constructor.
# my_list = ["Shade", "energy", "magnet", "Charse", "energy"]
# my_list2 = list((12, 14, "Sunday", "Charse", True, False, 5.08))
# my_list3 = [1, 45, 54, 23, 67, 78, 46]

# print(my_list)
# print(type(my_list))

# print(my_list2)
# print(my_list[3])


# my_list[1] = "solar"
# my_list[-2] = 'paul'
# print(my_list)
# print(my_list[2:3])
# print(my_list2[-3])
# print(my_list[-4:-1])
# my_list = ["Shade", "energy", "magnet", "Charse", "energy"]
# # print(len(my_list))
# # print(type(my_list2))
# if "shade" in my_list:
#   print("present")
# else:
#   print("not available")
# my_list.append(250)
# print(my_list)

# my_list = ["Shade", "energy", "magnet", "Charse", "energy"]
# my_list2 = list((12, 14, "Sunday", "Charse", True, False, 5.08))
# # my_list3 = [1, 45, 54, 23, 67, 78, 46]

# my_list.insert(3, "tunde")
# print(my_list)
# my_list.extend(my_xlist2)
# print(my_list)
# my_list.append(my_list2)
# print(my_list)
# for name in my_list2:
#     my_list.append(name)
# print(my_list)
# my_list.remove("energy") # remove is an inbuilt attribute of python object
# print(my_list)
# my_list2.pop(3)
# print(my_list2)
# my_list2.pop()
# print(my_list2)
# my_list = ["Shade", "energy", "magnet", "Charse", "energy"]
# my_list2 = list((12, 14, "Sunday", "Charse", True, False, 5.08))
# my_list3 = [1, 45, 54, 23, 67, 78, 46]
# my_list2.clear()
# print(my_list2)
# del my_list2
# print(my_list2)
# my_list3.sort()
# print(my_list3)
# my_list3.sort(reverse=True)
# print(my_list3)
# my_list = ["Shade", "shade", "Energy", "magnet", "Magnet", "Charse", "energy"]
# my_list.sort(reverse=True, key=str.lower)

# print(my_list)


# my_list = ["Shade", "energy", "magnet", "Charse", "energy"]
# my_list2 = list((12, 14, "Sunday", "Charse", True, False, 5.08))
# my_list3 = [1, 45, 54, 23, 67, 78, 46]
# print(my_list3)
# print(type(my_list3))
# con = tuple(my_list3)
# print(con)
# print(type(con))
# my_list2.reverse()
# print(my_list2)
# name = my_list2.copy()
# print(name)
# name = list(my_list2)
# print(name)
# name = my_list + my_list2
# print(name)
# print(my_list.count("energy"))
# print(max(my_list3))
# print(min(my_list3))
# my_list = ["Shade", "energy", "magnet", "Charse", "energy"]
# # print(my_list.index("magnet"))
# my_list = ["Shade", "energy", "magnet", "Charse", "energy"]
# my_list2 = list((12, 14, "Sunday", "Charse", True, False, 5.08))
# my_list3 = [1, 45, 54, 23, 67, 78, 46]
# my_list4 = [my_list, my_list2,my_list3, ['Favour', 34],my_list2, 'Tunde', False]
# # print(my_list4)
# [['Shade', 'energy', 'magnet', 'Charse', 'energy'], [12, 14, 'Sunday', 'Charse', True, False, 5.08], ['Favour', 34], 'Tunde', False]
# print(my_list4[2][-1])
# print(my_list4[4][4])
# print(my_list4[-4:-1])


"""
Assignment to be submitted on monday

write a python program that will set questions, set answers, ask user for answers
mark the answers, if the user get a question, your program should be able
to score the user 10 marks, and for every question missed, the program should minus
5 marks from the user's original score.
"""
