#  Tuple: A tuple is a collection that is ordered but not changeable. 
# # A tuple is created using
# #  braces i.e () or tuple()
# # mylist = ("ade", "femi")
# # print(mylist[1])
# name = ("Shade", "energy", "magnet", "Charse", "energy")
# name2 = tuple((12, 14, 1, "Sunday", "Charse",False, 5.08))
# print(name[2])
# print(name)
# print(type(name))
# print(name2)
# print(type(name2))
# print(name[3])
# print(name[1:4])
# print(name[-3])
# print(name[-3:-1])
# print(len(name))
# food = ('Yam',)
# print(food)
# print(type(name2))
# if "True" in name2:
#   print("is available")
# else:
#   print('not available')
# print(name)
name = ("Shade", "energy", "magnet", "Charse", "energy")
nm = list(name)
# nm.pop()
# print(nm)
# nm[3] = 'wine'
# nm.append("toy")
# print(nm)
# print(nm)
# name[3] = "wine"
# print(name)
# name.add("toy") # tuple has no attribute add error
# name.pop() # tuple has no attribute pop error
# name = ("Shade", "energy", "magnet", "Charse", "energy")
# del name
# print(name)

# Unpacking values of a tuple
# item = ("Ola", "22", "07064203742")
# (name, *phonenumber) = item
# print(phonenumber)
item = ("Yam", "Sunday", "Lagos","Yam", "Sunday", "Lagos", 45)
(food, name, location, *age) = item
# print(age)
# print('food: ', food)
# print('location:', location)
# print(len(item))
# (food, *name, age, mymy, our) = item
# print(name)
# (*name, ) = item
# print(name)

# for na in item:
#   print(na)
name = ("Shade", "energy", "magnet", "Charse", "energy")
name2 = tuple((12, 14, 1, "Sunday", "Charse",False, 5.08))
# new_name = name + name2
# print(new_name)
# print(type(new_name))
# new_name = name * 3
# print(new_name)
# print(name.count("energy"))
# name = ("Shade", "energy", "magnet", "Charse", "energy")
# # name2 = tuple((12, 14, 1, "Sunday", "Charse",False, 5.08))
# print(name.index("magnet"))

# fruits = tuple(('Name', 'name', 'age', 12, 'Age'))
# print(fruits.index('name'))

# Set: A set is a collection which is unordered and unindexed.
#  It is written using curly bracket
# i.e {} or set()
name = {"Shade", "energy", "magnet", "Charse",  "Charse", "energy"}
name2 = set((12, 14, "Sunday", "Charse", True, False, 5.08))
# print(name)
# # print(name2)
# print(len(name))

# print(type(name2))
# for top in name2:
#     print(top)
# print("Charse" in name)
# print("student" not in name)
# name.add("orange")
# print(name)
# name.update(name2)
# print(name)
# new_name = tuple(name) + tuple(name2)
# print(new_name)
# (name.add(name2))
# print(name)
# new_name = ["food", "drink", "dress", "wears"]
# name.update(new_name)
# print(name)
# print(type(name))
# name = {"Shade", "energy", "magnet", "Charse",  "Charse", "energy"}
# name2 = set((12, 14, "Sunday", "Charse", True, False, 5.08))
# name.update(("mango", "apple", "leave"))
# print(name)
# print(type(name))
# name = {"Shade", "energy", "Charse", "magnet", "energy", "see"}
# name2 = set((12, 14, "Sunday", "Charse", True, False, 5.08))
# name.remove("see")
# print(name)

# result = []
# for i in range(5):
#     inp = input("enter any number>> ")
#     result.append(inp)
#     print(result) #this indentation here will be printing at every stage of iteration

# students = []
# for i in range(5):
#     name = input("Enter your name ")
#     students.append(name)
# print(students) #this indentation here will print at the end of iteration
# students = set()
# for i in range(3):
#     enter = input("Enter your name")
#     students.update(enter) #this type of operation cannot be performed using set()
#     print(students)
name = {"Shade", "energy", "Charse", "magnet", "energy", "see"}
# name2 = set((12, 14, "Sunday", "Charse", True, False, 5.08))
# name.discard("see")
# print(name)
# name.pop()
# print(name)
# name.clear()
# print(name)
# del name
# print(name)
# name = {"Shade", "energy", "Charse", "magnet", "energy"}
# # name2 = set((12, 14, "Sunday", "Charse", True, False, 5.08))
# for y in name:
    # print(y)
    # print(type(y))

# set1 = {1, 90, 2} 


# comment = f""" commented that This is a python class. it was started 
#           last week and still continue through
#           this week. the number of people in this class is """
# new = comment.split()
# # print(new)
# t = tuple(new)
# # print(t)
# s = set(t)
# print(s)
# new_input = set(input('Enter here: ').split())

# print(yes)
# set1 = {6, 1, 2, 3, 4, 5}
# set2 = {1, 4, 5}
# inter = set2.intersection(set1)
# print(inter)
set1 = {2, 8, 6, 4}
set2 = {2, 4, 50, 5, 7, 8,12, 13}
set3 = {20, 50, 60}

# set4 = set1.union(set2).union(set3)
# print(set4)
# set3.update(set2)
# print(set3)
# print('Set1:', set1)
# print('Set2:', set2)
# print('Set3:', set3)
# intercept = set1.intersection((set2))
# print(intercept)
# intercept = set1.intersection((set2)).intersection((set3))
# print(intercept)
# set1.update(set2)
# print('Result:', set1)

set2 = {2, 4, 50, 5, 7, 8,12, 13}
set1 = {10, 50, 3, 4}
set3 = {10, 3, 4, 20, 50, 60}
# set4 = set1.symmetric_difference(set2)
# print('s_d:', set4)
# set2.symmetric_difference_update(set1)
# print('s_d_update:', set2)
# # set3.difference_update(set1)
# # print(set3)

# print(set1.isdisjoint(set2))
# print(set1.issubset(set3))
print(set3.issuperset(set1))

"""Write a python program that will ask user for their username and password, note, if the username and password is in your
the array of username and password, it should login, else invalid login details.
Furthermore, after login, your program should set theory questions,
ask user to provide answers, if user answer is the same as your answer, score the user and add 10 marks, else -5marks"""