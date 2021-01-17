text = input()
data = input()

while not data == "Done":
    command = data.split()[0]
    if command == "Change":
        char_to_find = data.split()[1]
        replacement = data.split()[2]
        text = text.replace(char_to_find, replacement)
        print(text)

    elif command == "Includes":
        str_to_check = data.split()[1]
        if str_to_check in text:
            print("True")
        else:
            print("False")

    elif command == "End":
        str_to_check = data.split()[1]
        if text.endswith(str_to_check):
            print("True")

        else:
            print("False")

    elif command == "Uppercase":
        text = text.upper()
        print(text)

    elif command == "FindIndex":
        char_to_check = data.split()[1]
        char_index = text.find(char_to_check)
        print(char_index)

    elif command == "Cut":
        start_index = int(data.split()[1])
        length = int(data.split()[2])
        text = text[start_index:(start_index+length)]
        print(text)
    data = input()
