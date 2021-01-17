from math import ceil

students_count = int(input())
lectures_count = int(input())
first_bonus = int(input())

max_point = 0
lectures_att = 0

while students_count > 0:
    curr_student = int(input())
    students_count -= 1
    # {total bonus} = {student attendances} / {course lectures} *(5 + {additional bonus})
    total_bonus = curr_student / lectures_count * (5 + first_bonus)
    if total_bonus > max_point:
        max_point = total_bonus
        lectures_att = curr_student

print(f"Max Bonus: {ceil(max_point)}.")
print(f"The student has attended {lectures_att} lectures.")