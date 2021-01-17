companions_count = int(input())
total_days = int(input())
curr_day = 1
total_coins = 0

while curr_day <= total_days:
    if curr_day % 10 == 0:
        companions_count -= 2
    if curr_day % 15 == 0:
        companions_count += 5
    total_coins += 50 - (2 * companions_count)
    if curr_day % 3 == 0:
        total_coins -= 3 * companions_count
    if curr_day % 5 == 0:
        total_coins += 20 * companions_count
        if curr_day % 3 == 0:
            total_coins -= 2 * companions_count
    curr_day += 1

coins = int(total_coins / companions_count)
print(f"{companions_count} companions received {coins} coins each.")