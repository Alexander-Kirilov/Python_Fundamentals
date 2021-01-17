first_emp = int(input())
second_emp = int(input())
third_emp = int(input())
sum_emp = first_emp + second_emp + third_emp
people_count = int(input())

time = 0

while people_count > 0:
    time += 1
    people_count -= sum_emp

    if time % 4 == 0:
        time += 1

print(f"Time needed: {time}h.")
