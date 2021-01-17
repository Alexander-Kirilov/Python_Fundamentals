import math

numbers = input().split(", ")
numbers = list(map(int, numbers))

max_num = max(numbers)
number_of_groups = math.ceil(max_num / 10)

for element in range(1, number_of_groups + 1):
    curr_range = []

    for num in numbers:
        upper = element * 10
        lower = upper - 10

        if lower < num <= upper:
            curr_range.append(num)

    print(f"Group of {element * 10}'s: {curr_range}")