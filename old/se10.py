numbers = [100, 23, 54, 8, 98, 13, 13, 23, 13]
total = 0
for n in numbers:
    total += n
print(total)
new_list = []
for n in numbers:
    if n > 20:
        new_list.append(n)

print(new_list)
print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(11 in numbers)
