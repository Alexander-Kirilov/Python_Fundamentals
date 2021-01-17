dungeons = input().split("|")
health = 100
bitcoins = 0
killed = False

for curr_room in dungeons:
    command, command_value = curr_room.split()
    command_value = int(command_value)

    if command == "potion":
        if command_value + health > 100:
            print(f"You healed for {(100-health)} hp.")
            health = 100
            print(f"Current health: {health} hp.")
            continue
        else:
            health += command_value
            print(f"You healed for {command_value} hp.")
            print(f"Current health: {health} hp.")

    elif command == "chest":
        print(f"You found {command_value} bitcoins.")
        bitcoins += command_value

    else:
        if health - command_value > 0:
            print(f"You slayed {command}.")
            health -= command_value
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {dungeons.index(curr_room)+1}")
            killed = True
            break

if not killed:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
