# username = input("Enter your username ")
# password = input("Enter your password ")
# print("Your registration is successful. You can proceed to the login page")
# logusername = input("ENter your username")
# logpassword  = input("ENter your password ")
# if logusername == username and logpassword == password:
#     print("Login successful")  
#     score = 0
#     questions = ["1. Who is the president of Nigeria?", "2. Who is the president of CBN?", "3. What is the name of the vice president of Nigeria?"]
#     options = ["a. President Umar Musa Yar'adua \n b. President Goodluck Ebele Jonanthan \n c. President Muhammad Buhari", "a. Godwin Ewemiewele \n b. Godwin Ewefiele \n c. Godwin Emefiele", "a. Joe Biden \n b. Yemi Osinbajo \n c. Jide Sanwoolu"]
#     answer = ["c", "c", "b"]
#     for quest in questions:
#         print(quest)
#         position = questions.index(quest)
#         print(options[position])
#         user_ans = input('Enter your answer ').lower()
#         correct_answer = answer[position]
#         if user_ans == correct_answer:
#             score += 10
#     print(f"Dear {username}, you scored {score}")
# else:
#     print("Invalid details")





# Dictionary: Dictionary is a collection which is ordered, changeable but does not allows
# duplicate and unindexed. Dictionary are used to store data in a key:value pairs.
# # It is written using {key:value} or dict(key=value)
# myNames = ["Ade", "boola"]
# myNames = {
#     "firstname" : "ade",
#     "secondname" : "shewa"
# }

# print(myNames["firstname"])
product = {
    "producer": "Toyota",
    "model": "venza 2021",
    "engine": "6 engine",
    "color": "black",
    "gear": 6,
    "ok": True,
}

# print(product["color"])
# myNames = {"Name1": "Nath", "Name2":"Michael"}
# print(myNames["Name1"])

# student_info = {1234: ["Taofeeq", "12", "Data science"]}
# print(student_info[1234])

# student_record = {"Isaac":["Male", 23, "Single to stupor"], "Taofeeq":["Male", 20, "Every lady is my goal"]}
# print(student_record["Taofeeq"][-3])

# s_r = {2035: ["Male", "Datascience", 12, 4, True]}

student_record = dict(
    name="Tony Johnson", level=300, course="mechanical engineering", subjects=10
)
# print('Student_record:', student_record)
# print(product)
# print(len(product))
# print(type(product))
# print(product["model"])
# print(product.get("model"))

# print(product.keys())
# print(product.values())

product = {
    "producer": "Toyota",
    "model": "nath 2026",
    "engine": "6 engine",
    "color": "black",
    "gear": 6,
    "ok": True,
}

# product["passenger"] = "ten"
# product["producer"] = "Nath"
# print(product)

# product["tyres"] = "4"
# print(product)
# print(student_record.items())
# print(student_record)
product = {
    "producer": "Toyota",
    "model": "venza 2021",
    "engine": "6 engine",
    "color": "black",
    "gear": 6,
    "ok": True,
}
student_record = dict(
    name="Tony Johnson", level=300, course="mechanical engineering", subjects=10
)
# print(student_record.values())
# print(0 not in student_record.values())
# product["engine"] = "lexus engine"
# product["air conditioner"] = "yes"
# product["producer"] = "lexus producer"
# print(product)
product.update({"year":2021, "color":"white", "speed": "500mph", "ok":False, "model": "Benz 2022"})
product["year"] = 2021
# print(product)
# product.pop('color')
# print(product)
# student_record.pop('course')
# print(student_record)
# print(product)
# product.popitem()
# print(product)
# del product["color"]
# print(product)
# product.clear()
# print(product)
# del product
# print(product)
# print(student_record)
product = {
    "producer": "Toyota",
    "model": "venza 2021",
    "engine": "6 engine",
    "color": "black",
    "gear": 6,
    "ok": True,
}
# student_record = dict(
#     name="Tony Johnson", level=300, course="mechanical engineering", subjects=10
# )
# print('Student_record:', student_record)

# for i in product:
#   print(i)

# for i in product:
#   print(product[i])
# for x in product.values():
#   print(x)
# for x in product.keys():
#   print(x)

# for x, y in product.items():
#     print(f"{x} :  {y}")
#     print("Hello")


# new_record = product
# print(new_record)
# new_record = dict(student_record)
# print(new_record)
student_details = {
  "Tony Johnson":{'name':'Tony Johnson', 'level':400, 'location':'Takie',
'dept':'math'},
  "Micheal Chan":{'name':'Micheal Chan', 'level':200, 'location':'General',
'dept':'computer'},
"Timi Joy":{'level':400, 'location':'Apake', 'dept':'english'}
}
# print(student_details.keys())
std1 = {'name':"Tony Johnson", 'level':300, 'location':'Takie', 'dept':'math'}
std2 = {'name':"Micheal Chan", 'level':200, 'location':'General', 'dept':'computer'}
student_details2 = {
  'FIRST_PERSON':std1,
  'SECOND_PERSON':std2
}
# print(student_details2['FIRST_PERSON'])
# print(student_details["Tony Johnson"])
# print(std1)
# print(student_details["Micheal Chan"]['location'])
# for record in student_details2['FIRST_PERSON']:
#   print(record)
# for record in student_details["Tony Johnson"].values():
#   print(record)

# ASSIGNMENT: Create a phonebook program that would allow the following operations: 1) Viewing the phonebook, 2) Adding to the phonebook 3) Deleting from the phonebook
