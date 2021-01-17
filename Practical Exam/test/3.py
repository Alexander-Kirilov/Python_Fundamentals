heroes = {}

data = input()

while not data == "Results":
    command = data.split(":")[0]
    if command == "Add":
        name = data.split(":")[1]
        health = int(data.split(":")[2])
        energy = int(data.split(":")[3])
        if name not in heroes:
            heroes[name] = {"health": health, "energy": energy}
        else:
            heroes[name]['health'] += health
    elif command == "Attack":
        attacker_name = data.split(":")[1]
        defender_name = data.split(":")[2]
        damage = int(data.split(":")[3])
        if attacker_name in heroes and defender_name in heroes:
            heroes[defender_name]['health'] -= damage
            if heroes[defender_name]['health'] <= 0:
                print(f"{defender_name} was disqualified!")
                del heroes[defender_name]

            heroes[attacker_name]['energy'] -= 1
            if heroes[attacker_name]['energy'] <= 0:
                print(f"{attacker_name} was disqualified!")
                del heroes[attacker_name]
        else:
            pass
    elif command == "Delete":
        user = data.split(":")[1]
        if user == "All":
            heroes = {}
        elif user in heroes:
            del heroes[user]
        else:
            pass

    data = input()

sorted_heroes = sorted(heroes.items(), key=lambda x: (-x[1]['health'], x[1]['energy'], x[0]))
print(f"People count: {len(heroes)}")
for name, value in sorted_heroes:
    print(f"{name} - {value['health']} - {value['energy']}")
