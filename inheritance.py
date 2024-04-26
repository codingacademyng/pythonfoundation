# PYTHON INHERITANCE
# Acquiring property from one class by another class.
# Inheritance allows us to define a class that inherits all the methods and property from another class.
# Parent class is the class being inherited from, also called "Base" class.
# The __init__() function is called automatically every time the class is being used to create a new object.
# Child class is the class that inherits from another class, also called the "Derived" class.
# We have two types; single and multi-level inheritance

# # for example;
class FirstClass:
    def __init__(self):
        print("Hello World")

    def display(self):
        print("Parent class")
    
    def learning(self):
        name = input("Enter the topic you're learning ")
        print(name)

class ChildClass(FirstClass):
    def something(self):
        print("Anything else")
    
# fc = FirstClass()
# ch = ChildClass()
# ch.display()
# ch.learning()
# ch.something()



class working:
    def __init__(self):
        print('Hello')
    
    def play(self):           #This is the parent class
        print("I am playing")
        


class walking(working):
    def __init__(self):
        print("Hey")
    def walk(self):
        print("I am walking")
        self.play()
    
# w = walking()
# w.walk()
# wo =working()
# # wo.play()
# wo.walk()
# w.walk()


class parent:
    def __init__(self):
        self.family_name = "Adeowo"
        self.name = "Owolabi"
        self.skin_color = "dark skin"
        self.height = "tall"
        self.language = "Yoruba"
        self.age = 50

    def walk(self):
        print(self.name + " from " + self.family_name + " is walking")

    def talk(self):
        print(self.name + " from " + self.family_name + "  is talking")

    def sleep(self):
        print(self.name + " is still sleeping")
    
    def old(self):
        print(self.name + " is " + str(self.age) + " years old")


class son(parent):
    def __init__(self):
        parent.__init__(self)
        self.name = "John"
        self.age = 13

    def jump(self):
        print(self.name + " is jumping up and down")

# so = son()
# so.old()
# so.jump()
# fa = parent()
# fa.old()
# fa.walk()
# fa.walk()
# ch.jump()


# # MULTILEVEL INHERITANCE


class grandFather:
    def __init__(self):
        self.family_name = "Adeowo"
        self.name = "Owolabi"
        self.skin_color = "dark skin"
        self.height = "tall"
        self.language = "Yoruba"
        self.age = 90
    def walk(self):
        print(self.name + " from " + self.family_name + " is walking")

    def talk(self):
        print(self.name + " from " + self.family_name + "  is talking")

    def sleep(self):
        print(self.name + " is still sleeping")


class father(grandFather):
    def __init__(self):
        # grandFather.__init__(self)
        super().__init__()
        self.age = 50
        self.name = "John"
        self.occupation = "Armed robbery"
        self.skin_color = "light skin"
        self.height = 'short'

    def jump(self):
        print(self.name + " is jumping up and down")

    def occupat(self):
        print(self.name + "'s occupation is " + self.occupation)
    
    def get_age(self):
        print(f"{self.name} is {self.age} years old")


class child(father):
    def __init__(self):
        super().__init__()
        self.name = "Micheal"
        self.height = "short"
        self.skin_color = "black"
        self.occupation = "Data Analyst"

    def run(self):
        print(self.name + " is running up and down")

    def description(self, age):
        print(
            "My name is "
            + self.name
            + " from "
            + self.family_name
            + " family and i am very "
            + self.height
            + " and he is " + str(age) + " years old"
        )
        self.walk()
    def getage(self):
        print(f"{self.name} is {self.skin_color} in complexion")
    
    def get(self):
        print(f"{self.name} is {self.age} years old and he is  {self.skin_color} in complexion")

# fa = father()
# print(fa.language)
ch =child()
# print(ch.language)
# ch.description(30)
# ch.walk()
# ch.get_age()
# gf = grandFather()
# ch.occupat()
# ch.get()

# ch = child()
# fa = father()
# gf = grandFather()
# # fa.talk()
# ch.description()
# ch.run()
# ch.occupat()
# fa.occupat()
# ch.walk()
# fa.walk()

# gf.walk()

# The object allows you to call on any of the family that you want to work on for instance, ch was used to represent the child
# fa was used to represent the father while gf was used to represent the grandFather. When function is called for these three objects:
# ch.walk()
# fa.walk()
# gf.walk()
# These 3 will print different name as the self.name of the three classes are different. the output will be:
# Micheal from Adeowo family is walking
# John from Adeowo family is walking
# Owolabi from Adeowo family is walking


# Python Module
# The module is like the code library. It serves as save for files containing a set of functions you want to include in your application.
# How to create module
#  you can create a module outside the file that you're' working on and save it. Then import the code into another work.
# it is imported by writing the word "import" then the name of the file e.g

# import practice
# practice.calc(2, 3)
# practice.hey()
# import practice as p
# p.hey()
# from practice import hey
# hey()

class operation:
    def __init__(self):
        self.var1 = int(input("Enter Value 1: "))
        self.var2 = int(input("Enter Value 2: "))
    
    def addition(self):
        print(self.var1 + self.var2)

    def subtraction(self):
        print(self.var1 - self.var2)

class further(operation):
    def __init__(self):
        operation.__init__(self)
        # super().__init__()
        self.var1 = 30
        self.var3 = int(input("Enter value 3 "))

    def multiplication(self):
        print(self.var3 * self.var1)

# op = operation()
# op.addition()
# fur = further()
# fur.addition()
# fur.multiplication()
# fur.addition()
# # op = operation()
# # op.addition()
# fu = further()
# # fur.addition()




# user_name = ["ola", "seun"]
# password =["1234", "5678"]
# age = [15, 25]
# zipLi = list(zip(user_name, password, age))
# print(zipLi)

def login():
    user_name = ["ola", "seun"]
    password =["1234", "5678"]
    log = list(zip(user_name, password))
    print(log)
    user = input("Enter your username ")
    pas = input("Enter your password ")
    if (user, pas) in log:
        print("Login successful")
        # from exam_cbt import exam
        # exam()
    else:
        print("Login failed")
# login()

# Python Math class
# import math
l = [2, 4, 5, 7, 3]
# print(min(l))
# print(max(l))
# print(abs(-5.34))
# print(pow(5, 3))
# print(math.sqrt(9))
# print(math.ceil(6.001))
# print(math.floor(5.9999999999))
# print(math.pi)
# print(math.floor(math.pi * 1000 + 25))


# CREATING A NEW LIST FROM ONE LIST
# myList = ["shade", "ola", "bayo", "feyi", "tope"]
# newList = []
# for names in myList:
#     if "a" in names:
#         newList.append(names)

# newList = [names for names in myList if "a" in names]
# print(newList

# numList = []

# for i in range (1, 21):
#     numList.append(i)

# numList = [i for i in range(1, 21)]
# print(numList)


# ZIP
# username = ["ade", "shola", "tunde"]
# passwds = [20, 10, 15]

# collateInfo = list(zip(username, passwds))
# print(collateInfo)

# use = input("Enter your use ")
# pwd = int(input("Enter your pass "))

# if (use, pwd) in collateInfo:
#     print("Login successful")
# else:
#     print("Invalid username or password")



# Design a betting application that includes user registration and login functionalities. Upon registration, each user starts with a default balance of zero. Once logged in, users can perform the following actions: Deposit Money, Check Balance, and Place Bets. The betting feature operates as follows: The system generates three random colors, and the user must select an amount to wager, which cannot exceed their current balance. Subsequently, the user is prompted to choose three colors. If all three colors selected by the user match the computer's random choices, the user's winnings increase by a factor of 6 i.e amount staked times 6. If two colors match, the user's winnings increase by a factor of 4, and if only one color matches, the winnings increase by a factor of 2. However, if none of the user's chosen colors match the computer's selections, the user loses the amount they wagered on the bet. Good luck.


# class Products:
#     def __init__(self):
#         self.name = "Goods"
#         self.age = 20

#     def viewItem(self):
#         print("You are viewing " + self.name)

# class Shoe(Products):
#     def __init__(self):
#         Products.__init__(self)
#         self.name = "Shoe"

# class Bag(Products):
#     def __init__(self):
#         Products.__init__(self)
#         self.name = "Bag"

# shoe = Shoe()
# bag = Bag()

# bag.viewItem()
# shoe.viewItem()

# print(bag.age)

# def start():
#     print("Hello world")
# start()

class Obj:
    def __init__(self):
        self.name = "Shade"
        self.age = 30
        

    def start(self):
        print("Hello World")
        print(self.age)
    
    def login(self):
        self.username = input("ENter your username ")

# myObj = Obj()
# myObj.start()
# print(myObj.name)

class childObj(Obj):
    def __init__(self):
        super().__init__()
        self.age = 20
    def walk(self):
        print("SOmething")

# ch = childObj()
# ch.start()

# properties = [{'price_in_usd': 68663.03, 'area_in_m2': 208, 'room_num': 3}, {'price_in_usd': 100412.94, 'area_in_m2': 256, 'room_num': 4}, {'price_in_usd': 41967.85, 'area_in_m2': 87, 'room_num': 4}, {'price_in_usd': 80186.97, 'area_in_m2': 158, 'room_num': 2}, {'price_in_usd': 48405.36, 'area_in_m2': 249, 'room_num': 3}]
# for prpty in properties:
#     price_per_m2 = prpty.get("price_in_usd") / prpty.get("area_in_m2")
#     prpty.update({"price_per_m2":price_per_m2})
# print(properties)

def sqaure_odd(x):
    # newList = []
    if type(x) == list:
    #     for num in x:
    #         if num % 2 != 0:
    #             square_num = num * num
    #             newList.append(square_num)
        newList = [num * num for num in x if num % 2 != 0]
        print(newList)
    else:
        print("Funtion only requires a list")

# sqaure_odd(2)
# rangelist = [x for x in range(1, 51)]
# sqaure_odd([2, 3, 4, 5])
# sqaure_odd([9, 2, 5,  10, 3, 45])
# sqaure_odd(rangelist)
