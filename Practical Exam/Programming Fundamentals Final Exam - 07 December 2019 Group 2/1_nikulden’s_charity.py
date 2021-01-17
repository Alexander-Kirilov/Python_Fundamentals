def is_valid(index, limit):
    return 0 <= index < limit


text = input()
command = input()

while not command == "Finish":
    command = command.split()
    action = command[0]
    if action == "Replace":
        text = text.replace(command[1], command[2])
        print(text)
    elif action == "Cut":
        subtext = list(text)
        start = int(command[1])
        stop = int(command[2])
        if is_valid(start, len(text)) and is_valid(stop, len(text)):
            if text[start:stop + 1]:
                for i in range(start, stop + 1):
                    subtext[i] = "Delete"
                text = "".join(ch for ch in subtext if ch != "Delete")
                print(text)
            else:
                print("Invalid indexes!")
        else:
            print("Invalid indexes!")
    elif action == "Make":
        if command[1] == "Upper":
            text = text.upper()
        elif command[1] == "Lower":
            text = text.lower()
        print(text)
    elif action == "Check":
        if command[1] in text:
            print(f"Message contains {command[1]}")
        else:
            print(f"Message doesn't contain {command[1]}")
    elif action == "Sum":
        start = int(command[1])
        stop = int(command[2])
        if is_valid(start, len(text)) and is_valid(stop, len(text)):
            if text[start:stop + 1]:
                subtext = list(text[start:stop + 1])
                total = sum([ord(i) for i in subtext])
                print(total)
            else:
                print("Invalid indexes!")
        else:
            print("Invalid indexes!")
    command = input()
