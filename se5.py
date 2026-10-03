# age = 18

# if age >= 18:
#     print("you are adult")
#     print("you can Drive")
# print("This line always  executes")


# password = input("Enter your password: ")
# if password == "python123":
#     print("Welcome")
#     print("You Logged In")
# else:
#     print("Password is not correct")
#     print("You are not a valid user")


# num = int(input("Enter the number: "))
# if num % 2 == 0:
#     print(f"{num} is Even")
# else:
#     print(f"{num} is Odd")

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > b : 
#     print(f"{a} is greater than {b}")
# else:
#     print(f"{b} is greater than {a}")


# score = float(input("Enter your score "))
# if score >= 90:
#     print("*****")
#     print("Great")
# elif score >= 80:
#     print("****")
#     print("Good")
# elif score >= 70:
#     print("***")
#     print("Not Too Good")
# elif score >= 60:
#     print("**")
#     print("Not Bad")
# else:
#     print("you Failed")


# age = 18
# has_li = True

# if age >= 18 or has_li == True:
#     print("you can drive")

# is_raining = False
# if not is_raining:
#     print("we can go park")

import random


secret = random.randint(1,10)
guess = int(input("enter a number from 1 to 10: "))
if guess > secret:
    print(f"your guess is {guess - secret} number greater than secret number")
elif guess < secret:
    print(f"your guess is {secret - guess} number lower than secret number")
else:
    print("Thats Right")