events = input().split("|")

energy = 100
coins: int = 100
is_valid = False

for event in events:
    event_type, event_value = event.split("-")
    event_value = int(event_value)

    if event_type == "rest":
        energy += event_value
        if energy > 100:
            energy = 100
            print(f"You gained {0} energy.\nCurrent energy: {energy}.")
        else:
            print(f"You gained {event_value} energy.\nCurrent energy: {energy}.")
    elif event_type == "order":
        energy -= 30
        if energy >= 0:
            coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        if coins >= event_value:
            coins -= event_value
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}.")
            is_valid = True
            break

if is_valid:
    pass
else:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")