# try:
#     a = int(input("enter a number: "))
#     b = int(input("enter a number: "))

#     print(a + b)
# except:
#     print("invalid input")
#     print(0)

# import time

# while True:
#     print("hello")
#     time.sleep(1)
import random

all_choices = ("r", "p", "s")
computer_choice = random.choice(all_choices)
user_choice = input("enter r p s : ")
print("computer: ", computer_choice)
print("user:", user_choice)


# with open("myfile.txt", "w") as f:
#     f.write("hello")

# with open("myfile.txt", "r") as f:
#     print(f.read())

# username = input("enter the username: ")
# password = input("enter the password: ")

# with open("user.txt", "w") as f:
#     f.write(username + "\n")
#     f.write(password + "\n")
# try:
#     with open("user.txt", "r") as myfile:
#         username = myfile.readline().strip()
#         password = myfile.readline().strip()
#     print(username, password)
# except:
#     print("file not found error")


# x = int(input("enter a number: "))
# y = int(input("enter a number: "))
# try:
#     print(x / y)
# except:
#     print("undefined")

# import random

# print(random.randint(1, 10))
# fruits = ["orange", "apple", "banana"]
# print(random.choice(fruits))
# import math

# print(math.pi)
# print(pow(2, 3))
# print(math.ceil(2.1))
# print(math.floor(2.1))
# print(abs(-7))
# print(math.fabs(-7))
# from datetime import datetime, date

# print(datetime.now())
# birthday = date(2000, 10, 10)
# print(birthday)
# import os

# print(os.getcwd())
# print(os.listdir())
