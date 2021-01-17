def replace_upper(key, str_to_replace):
    return key.replace(str_to_replace, str_to_replace.upper())


def replace_lower(key, str):
    return key.replace(str_to_replace, str_to_replace.lower())


# def str_slice(key, str):
#     return key.replace(str, key)
#

activation_key = input()

data = input()

while not data == "Generate":
    command = data.split(">>>")[0]

    if command == "Contains":
        substring = data.split(">>>")[1]
        if substring not in activation_key:
            print("Substring not found!")
        else:
            print(f"{activation_key} contains {substring}")

    elif command == "Flip":
        sec_command = data.split(">>>")[1]
        start_index = int(data.split(">>>")[2])
        end_index = int(data.split(">>>")[3])
        if sec_command == "Upper":
            str_to_replace = activation_key[start_index:end_index]
            activation_key = replace_upper(activation_key, str_to_replace)
        elif sec_command == "Lower":
            str_to_replace = activation_key[start_index:end_index]
            activation_key = replace_lower(activation_key, str_to_replace)
        print(activation_key)

    elif command == "Slice":
        start_index = int(data.split(">>>")[1])
        end_index = int(data.split(">>>")[2])
        str_to_replace = activation_key[start_index:end_index]
        activation_key = activation_key.replace(str_to_replace, '')
        print(activation_key)
    data = input()

print(f"Your activation key is: {activation_key}")