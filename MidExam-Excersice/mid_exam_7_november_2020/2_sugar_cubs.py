all_cubes = input().split(" ")

data = input()
while not data == "Mort":
    command = data.split(" ")[0]
    value = data.split(" ")[1]

    if command == "Add":
        all_cubes.append(value)
    elif command == "Remove":
        all_cubes.remove(value)
    elif command == "Replace":
        replacement = data.split(" ")[2]
        index_to_take = all_cubes.index(value)
        all_cubes.insert(index_to_take, replacement)
        all_cubes.remove(value)
    elif command == "Collapse":
        all_cubes_int = list(map(int, all_cubes))
        value = int(value)
        all_cubes_int[:] = [x for x in all_cubes_int if x >= value]
        all_cubes = list(map(str, all_cubes_int))
    data = input()

print(' '.join(all_cubes))

