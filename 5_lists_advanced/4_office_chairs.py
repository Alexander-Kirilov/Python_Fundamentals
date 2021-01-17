count_of_rooms = int(input())
total_free_chairs = 0
is_valid = True

for curr_room in range(1, count_of_rooms + 1):
    room_data = input().split()
    chairs_count = len(room_data[0])
    number_of_people = int(room_data[1])

    if chairs_count >= number_of_people:
        total_free_chairs += chairs_count - number_of_people

    else:
        needed_chairs_in_room = number_of_people - chairs_count
        total_free_chairs -= needed_chairs_in_room
        print(f"{needed_chairs_in_room} more chairs needed in room {curr_room}")
        is_valid = False

if is_valid:
    print(f"Game On, {total_free_chairs} free chairs left")
