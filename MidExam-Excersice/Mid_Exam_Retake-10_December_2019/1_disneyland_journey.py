journey_cost = float(input())
months_to_collect = int(input())

collected_money = 0

for curr_month in range(1, months_to_collect + 1):
    if curr_month == 1:
        collected_money += journey_cost * 0.25
        continue
    if not curr_month % 2 == 0:
        collected_money -= collected_money * 0.16
    if curr_month % 4 == 0:
        collected_money += collected_money*0.25

    collected_money += journey_cost * 0.25

if collected_money > journey_cost:
    saved_money = collected_money - journey_cost
    print(f"Bravo! You can go to Disneyland and you will have {saved_money:.2f}lv. for souvenirs.")
else:
    money_needed = journey_cost-collected_money
    print(f"Sorry. You need {money_needed:.2f}lv. more.")
