lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_expenses = 0
curr_lost = 1

while curr_lost <= lost_fights_count:
    if curr_lost % 2 == 0:
        total_expenses += 1 * helmet_price
    if curr_lost % 3 == 0:
        total_expenses += 1 * sword_price
    if curr_lost % 6 == 0:
        total_expenses += 1 * shield_price
    if curr_lost % 12 == 0:
        total_expenses += 1 * armor_price
    curr_lost += 1

print(f"Gladiator expenses: {total_expenses:.2f} aureus")
