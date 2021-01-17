all_numbers = list(map(int, input().split()))
# 29 13 9 0 13 0 21 0 14 82 12
left_racer = []
right_racer = []
zero_penalty_left = 0
zero_penalty_right = 0

curr_total_right = sum(right_racer)

half = len(all_numbers) // 2
for index in range(0, half):
    left_racer.append(all_numbers[index])
    if all_numbers[index] == 0:
        zero_penalty_left = sum(left_racer) - (sum(left_racer) * 0.80)

reversed_list = list(reversed(all_numbers))
for index in range(0, half):
    right_racer.append(reversed_list[index])
    if all_numbers[index] == 0:
        zero_penalty_right = sum(right_racer) - (sum(right_racer) * 0.80)

total_left = sum(left_racer) - zero_penalty_left
total_right = sum(right_racer) - zero_penalty_right

if total_left < total_right:
    print(f"The winner is left with total time: {total_left:.1f}")
else:
    print(f"The winner is right with total time: {total_right:.1f}")
