# count = 1
# while count <= 5:
#     print(count)
#     # count = count + 1
#     count += 1

# n = int(input("enter a number: "))
# total = 0
# i = 1
# while i <= n:
#     total += i
#     i += 1
# print(total)
import random
secret  = random.randint(1,10)
attempts = 0
print("guess a number between 1 - 10: ")
while True:
    guess = int(input("guess: "))
    attempts += 1
    if guess == secret:
        print(f"good you find it after {attempts} times")
        break
    elif guess < secret:
        print("your guess is lower")
    else:
        print("your guess is greater")