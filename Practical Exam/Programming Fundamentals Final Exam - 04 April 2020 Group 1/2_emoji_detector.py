import re

regex = r"([:]{2}|[*]{2})(?P<emoji>[A-Z][a-z]{2,})(\1)"
string = input()
cool_threshold = 1
regex_digits = r"\d"

digits = re.findall(regex_digits, string)

for digit in digits:
    cool_threshold *= int(digit)
print(f"Cool threshold: {cool_threshold}")

emojis = re.finditer(regex, string)
full_emojis = [e.group() for e in emojis]
print(f"{len(full_emojis)} emojis found in the text. The cool ones are:")

cool_emojis = []
for emoji in full_emojis:
    emoji_coolness = 0
    for char in emoji:
        if char != ":" and char != "*":
            emoji_coolness += ord(char)
    if emoji_coolness > cool_threshold:
        cool_emojis.append(emoji)

for emoji in cool_emojis:
    print(emoji)