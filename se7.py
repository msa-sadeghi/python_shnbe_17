# name= "python"
# for letter in name:
#     print(letter)

# fruits = ["apple", "orange", "banana"]
# for f in fruits:
#     print(f)

# for i in range(5):
#     print(i)


# for number in range(10):
#     print(number)

# for number in range(1, 10):
#     print(number)

# for number in range(1, 10, 2):
#     print(number)

# for number in range(10, 0, -1):
#     print(number)


n = int(input("enter a number: "))
for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")


count = int(input("How many numbers you want to enter: "))
total = 0
maximum = None
minimum = None
for i in range(count):
    num = int(input(f"Enter Number {i+1}: "))
    total += num
    if maximum is None or num > maximum:
        maximum = num
    if minimum is None or num < minimum:
        minimum = num

print(f"total is :{total}")
print(f"average is :{total/count :.2f}")
print(f"minimum is :{minimum}")
print(f"maximum is :{maximum}")
