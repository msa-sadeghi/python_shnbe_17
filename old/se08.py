# numbers = [3, 7, 11, 4, 9, 2, 8]
# for n in numbers:
#     if n % 2 == 0:
#         print(f"first even :  {n}")
#         break
#     print(f"{n} is odd")

# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     print(i, end=" ")

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} * {j} = {i*j}", end="   ")
#     print()

import turtle

for i in range(3):
    turtle.forward(100)
    turtle.left(120)

turtle.done()