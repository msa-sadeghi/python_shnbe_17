# point = (10, 20)
# colors = ("blue", "green", "red")
# single = (42,)

# print(point[0])
# print(colors[-1])
# print(colors[1:])

# nums = {1,2,3,4,5,6,3}
# nums.add(100)
# nums.remove(1)
# print(nums)

# favorite_sports = {
#     "reza":"football",
#     "sara":"football",
#     "amir":"baseball"
# }
# print(f"reza likes {favorite_sports['reza']}")
# print(f"sara likes {favorite_sports['sara']}")
# print(f"amir likes {favorite_sports['amir']}")

# student = {
#     "name" : "ali",
#     "age" : 16,
#     "city" : "tehran",
#     "score" : 92.4,
#     "active" : True
# }
# print(student["name"])
# student["score"] = 96
# student["grade"] = "A"
# del student["active"]
# student.pop("age")
# print(student)



student = {
    "name" : "ali",
    "age" : 16,
    "city" : "tehran",
    "score" : 92.4,
    "active" : True
}

for item in student:
    print(item)

for item in student.values():
    print(item)
for item in student.items():
    print(item)
for key, val in student.items():
    print(key, val)