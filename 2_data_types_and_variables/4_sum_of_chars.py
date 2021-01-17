number_of_lines = int(input())
total_sum = 0

while number_of_lines > 0:
    total_sum += int(ord(input()))
    number_of_lines -= 1

print(f"The sum equals: {total_sum}")