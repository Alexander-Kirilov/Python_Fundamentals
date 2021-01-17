text_input = input()
unliked_meals_count = 0
guests = {}

while text_input != "Stop":
    command, guest, meal = text_input.split("-")

    if command == "Like":

        if guest not in guests:
            guests[guest] = []
        if meal in guests[guest]:
            text_input = input()
            continue

        guests[guest].append(meal)

    elif command == "Unlike":

        if guest not in guests:
            print(f"{guest} is not at the party.")
            text_input = input()
            continue

        if meal not in guests[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
            text_input = input()
            continue

        guests[guest].remove(meal)
        unliked_meals_count += 1
        print(f"{guest} doesn't like the {meal}.")

    text_input = input()

guests = dict(sorted(guests.items(), key=lambda g: (-len(g[1]), g[0])))

for guest, meals in guests.items():
    print(f"{guest}: {', '.join(meals)}")

print(f"Unliked meals: {unliked_meals_count}")
