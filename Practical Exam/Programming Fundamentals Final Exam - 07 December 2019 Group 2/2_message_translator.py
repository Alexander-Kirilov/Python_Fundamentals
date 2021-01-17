import re

count_of_mess = int(input())
text = input()

pattern = r"(?P<command>(?<=!)[A-Z][a-z]{2,}(?=!))!:\[(?P<message>(?<=\[)[a-zA-Z]{8,}(?=\]))"

for _ in range(count_of_mess-1):
    matches = re.finditer(pattern, text)
    current_message = [el.group['message'] for el in matches]
    if not current_message:
        print("The message is invalid")
    else:
        word_match = []
        matches = [word_match.append(word) for word in current_message]
        print(matches)
    text = input()
