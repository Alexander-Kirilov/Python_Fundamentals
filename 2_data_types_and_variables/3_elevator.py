import math

persons = int(input())
capacity = int(input())

if persons % capacity == 0:
    courses = persons / capacity
    print(round(courses))
else:
    courses = persons / capacity
    print(math.ceil(courses))
