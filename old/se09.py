# def greet(name):
#     print(f"Hello {name}, welcome")
#     print("Welcome to python class")

# greet("sara")
# greet("reza")


# def introduce(name, age, city):
#     print(f"name : {name}")
#     print(f"age : {age} year")
#     print(f"city : {city}")


# introduce("nikan", 10, "tehran")
# introduce("vihan", 5, "shiraz")


# def add(a, b):
#     return a + b


# x = add(1, 2)
# y = add(3, 4)

# print(add(x,y))



def is_even(n):
    return n % 2 == 0

print(is_even(4))
print(is_even(5))

def myfunction(n):
    if n > 0:
        sign = "positive"
    elif n < 0:
        sign = "negative"
    else:
        sign = "zero"
    result = is_even(n)
    if result == True:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"

    return f"{n} is {sign} and {even_or_odd} number"

print(myfunction(-4))
    
    