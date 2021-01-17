import re

n_inputs = int(input())

pattern = r"^([$%])([A-Z][a-z]{2,})\1: (?P<message>\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$)"

data = input()
for _ in range(1, n_inputs+1):
    matches = re.match(pattern, data)
    if matches:
        tag = matches[2]
        first_char = int(matches[4])
        second_char = int(matches[5])
        third_char = int(matches[6])

        decr_mess = []
        decr_mess.append(chr(first_char))
        decr_mess.append(chr(second_char))
        decr_mess.append(chr(third_char))
        decrypt_mess = ''.join(decr_mess)
        print(f"{tag}: {decrypt_mess}")

    else:
        print("Valid message not found!")
    if _ == n_inputs:
        break
    else:
        data = input()

