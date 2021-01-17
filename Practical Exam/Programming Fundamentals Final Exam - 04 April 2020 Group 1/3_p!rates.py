data = input()
towns = {}

while not data == "Sail":
    town, people, gold = data.split("||")
    people = int(people)
    gold = int(gold)
    if town not in towns:
        towns[town] = {'people': people, 'gold': gold}
    else:
        towns[town]['people'] += people
        towns[town]['gold'] += gold
    data = input()

data = input()
while not data == "End":
    command = data.split("=>")[0]
    if command == "Plunder":
        town = data.split("=>")[1]
        people = int(data.split("=>")[2])
        gold = int(data.split("=>")[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        towns[town]['people'] -= people
        towns[town]['gold'] -= gold
        if towns[town]['people'] and towns[town]['gold'] != 0:
            pass
        else:
            print(f"{town} has been wiped off the map!")
            del towns[town]
            data = input()
            continue

    elif command == "Prosper":
        town = data.split("=>")[1]
        gold = int(data.split("=>")[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            data = input()
            continue
        towns[town]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {towns[town]['gold']} gold.")
    data = input()

sorted_towns = sorted(towns.items(), key=lambda x: (-x[1]['gold'], x[0]))

if len(towns) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:")
for town, value in sorted_towns:
    print(f"{town} -> Population: {towns[town]['people']} citizens, Gold: {towns[town]['gold']} kg")
