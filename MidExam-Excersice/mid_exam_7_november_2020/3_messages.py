data = input()
all_chat = []

while not data == "end":
    command = data.split(" ")[0]
    message = data.split(" ")[1]

    if command == "Chat":
        all_chat.append(message)

    elif command == "Delete":
        if message in all_chat:
            all_chat.remove(message)

    elif command == "Edit":
        command, mess_to_edit, updated_ver = data.split(" ")
        if mess_to_edit in all_chat:
            index_to_edit = all_chat.index(mess_to_edit)
            all_chat.insert(index_to_edit, updated_ver)
            all_chat.remove(mess_to_edit)
        else:
            data = input()
            continue

    elif command == "Pin":
        mess_to_pin = message
        all_chat.remove(message)
        all_chat.append(mess_to_pin)

    elif command == "Spam":
        spam_list = data.split(" ")[1:]
        [all_chat.append(el) for el in spam_list]

    data = input()

print('\n'.join(all_chat))
