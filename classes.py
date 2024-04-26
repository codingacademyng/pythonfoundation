# Python Object Oriented Programming (OOP)
# OOP is to design the program using classes and objects.
# The object is related to real-word entities such as book pencil etc.
# the oop focuses on writing reuseable code. It is a widespread technique to solve the problem
# by creating objects. The major pricniples of OOP are class, object, inheritance etc
# Class can be defined as a collection of onjects. it is logical entity that has sojme speicific attibutes and methods E.g
# if you have an employee class, then it should contain an attribute and method i.e. email id, name, age, salary etc

# WHY OOP
# Makes code reuseable
# makes code organized

# self parameter is current to the instance of the class and is used to access variable that belongs to the class.

# Characteristics of class
# Object Attributes
# Object Methods (Functions)

# The reason you need to use self. is because Python does ot use special syntax to refer to instance attributes. Python decided to do methods in a way that makes the instance to
# which the method belongs be passed automatically, but not received automatically: The first parameters of methods is the instance the methiod is called on.

# def drive():
#     print("This car is moving")
# drive()
# class Car:
#     def drive(self):
#         print("This car is driving")


# Car().drive()
# name = "ade"
# print(name)
# class Car:
#     def __init__(self):
#         self.name = "ade"
#         self.age = 90
        
#     def move(self):
#         print("The car is moving")

# venza = Car()
# print(venza.name)
# Car().move()
# print(Car().name)
# print(Car().age)


class Info:
    def __init__(self):
        self.name = "ade"
        self.age = 20

    def playing(self):
        print(f"{self.name} is playing")

    def singing(self):
        print(f"{self.name} is singing")

# information=Info()
# information.singing()
# information.playing()
# print(information.name)
# class student_name:
#     def __init__(self):
#         self.name = "Philips"
#         self.age = 50
#         self.course = "Datascience"
#         self.pwd = "1234"
#         self.testing = input("Enter anythin ")
#     def names(self):
#         print(f"My name is {self.name}")
#         print(f"My age is {self.age}")
#         print(self.testing)
    
#     def sleep(self):
#         print(f"{self.name} is {self.age} years old, he is studying {self.course} and currently sleeping")
    
#     def login(self):
#         username = input("Enter your username: ").title()
#         password = input("Enter your password: ")
#         if username == self.name and password == self.pwd:
#             print("Login successful")
#         else:
#             print("Login failed")
#         print(self.testing)
    
# sn = student_name()
# sn.names()
# sn.sleep()
# sn.login()

# def addition(a, b):
#     sum = a + b
#     print(sum)

# addition(5, 10)

# def names(a):
#     print("My name is ", a)

# names("shade")

# class student_info:
#     name = "maya"
#     age = 50
#     course = "Datascience"
#     def ella(self):
#         print("My name is", self.name)

#     def names(self, x):
        
#         print("My name is ", x)
    
#     def new_name(self, y):
#         print("My name is ", y)
# std = student_info()
# std.ella()
# std.names("Shade")
# print(std.age)

# std.names("Ola")
# std.new_name("Isaac")
# print(std.course)
# std.ella()
# std.names("seun")
# std.names("ade")

# class Carr:
#     owner = "John Smith"
#     location = "Lagos"
#     gear = 5
#     tyre = 4

#     def run(self, value):
#         print("the car is running at full speed of " + value)

#     def pack(self):
#         print(f"the car just packed now and is currently in {self.location}")

# myCar = Carr()
# myCar.run(input("Enter the speed of the car "))
# myCar.pack()
# print(myCar.gear)

# Once a class is defined with Data and function, an object is created as
# an object to the class
# Instance variables are variables declared inside the class but
# not inside the function and can be accessed through class name or object

import time


class Car:
    def __init__(self):
        self.owner = "John Smith"
        self.location = "Ogbomoso"
        self.name = "Toyota"
        self.color = "Brown"
        self.brand = "2023 Model"
        self.trafficator = "Straight"
        self.tyre = 4
        self.stiring = 1
        self.gear = "0"
        self.speed = "10km/h"

    def details(self):
        print(
            "This car is owned by " + self.owner + " and is located in " + self.location
        )
        time.sleep(3)
        self.startEngine()

    def startEngine(self):
        print("The engine has started")
        time.sleep(2)
        self.gear = input("Enter gear 1 to take off: ")
        if self.gear == "1":
            self.moveCar()
        else:
            print("That is not the right gear to take off with")
            self.startEngine()

    def moveCar(self):
        print(
            self.name
            + " is in gear "
            + self.gear
            + " and the car is moving "
            + self.trafficator
            + " at a spead of "
            + self.speed
        )
        self.driver = input(
            "Press 'Y' to change gear, 'D' to change direction, 'S' to change Speed and 'P' to Park: "
        )
        if self.driver.upper() == "Y":
            self.changeGear()
        elif self.driver.upper() == "D":
            self.direction()
        elif self.driver.upper() == "S":
            self.changeSpeed()
        elif self.driver.upper() == "P":
            self.park()
        else:
            self.moveCar()

    def changeGear(self):
        self.gear = input("Enter gear number ")
        if self.gear == "1":
    
            self.moveCar()
        elif self.gear == "2":
            self.moveCar()
        elif self.gear == "3":
            self.moveCar()
        elif self.gear == "4":
            self.moveCar()
        else:
            print("This car does not have gear that exceed gear 4")
            self.changeGear()

    def direction(self):
        self.trafficator = input("Please enter your direction ")
        if self.trafficator.lower() == "straight":
            self.moveCar()
        elif self.trafficator.lower() == "left":
            self.moveCar()
        elif self.trafficator.lower() == "right":
            self.moveCar()

    def changeSpeed(self):
        newSpeed = int(input("Enter your speed "))
        if self.gear == "1" and newSpeed > 30:
            print("Incompatible speed, car cannot drive at high speed with gear 1")
            self.moveCar()
        elif self.gear == "2" and newSpeed > 60:
            print("Incompatible speed, car cannot drive at high speed with gear 2")
            self.moveCar()
        elif self.gear == "3" and (newSpeed > 120 or newSpeed < 60):
            print("Incompatible speed")
            self.moveCar()
        else:
            self.speed = str(newSpeed) + "km/h"
            self.moveCar()

    def park(self):
        print("Print the car is parking now....")
        time.sleep(2)
        print("The car has finished parking and application exited")


# cr=Car()
# cr.details()

# myCar.run('34 KM/H')


# def log():
#     global inp
#     inp = input("Enter username ")
#     sign()

# def sign():
#     print(inp)

# class App:
#     def log(self):
#         self.inp = input("Enter username ")
#         self.sign()  

#     def sign(self):
#         print(self.inp)

