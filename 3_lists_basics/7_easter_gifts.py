gift_planned = input().split()
command = input()

while not command == "No Money":
    if "OutOfStock" in command:
        command_name, gift = command.split()
        for index1 in range(len(gift_planned)):
            if gift_planned[index1] == gift:
                gift_planned[index1] = "None"

    elif "Required" in command:
        command_name, gift, index = command.split()
        index = int(index)
        if 0 <= index < len(gift_planned):
            gift_planned[index] = gift

    elif "JustInCase" in command:
        command_name, gift = command.split()
        gift_planned[-1] = gift

    command = input()

while 'None' in gift_planned:
    gift_planned.remove('None')

print(' '.join(gift_planned))