numbers_list = [element for element in input().split()]
user_text = list(input())

output_phrase = []

for element in numbers_list:

    element = [int(element) for element in element]

    if sum(element) > len(user_text):
        text_index = sum(element) - len(user_text)
        new_index = user_text[text_index]
        output_phrase.append(new_index)
        user_text.remove(new_index)
    else:
        new_index = user_text[sum(element)]
        output_phrase.append(new_index)
        user_text.remove(new_index)


print("".join(output_phrase))
