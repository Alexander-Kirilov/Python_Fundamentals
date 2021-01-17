text = input()
for i in range(len(text)):
    if text[i] == ':':
        print(f":{text[i + 1]}")

# цикъла е елементарен и може да се направи с comprehension.
# [print(f":{text[i + 1]}") for i in range(len(text)) if text[i] == ':']