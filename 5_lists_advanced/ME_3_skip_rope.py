secret_message = input()

numbers_list = [el for el in secret_message if el.isdigit()]
not_number_list = [el for el in secret_message if el.isalpha()]

nums_as_int = list(map(int, numbers_list))
take_list = [nums_as_int[index] for index in range(len(nums_as_int)) if index % 2 == 0]
skip_list = [nums_as_int[index] for index in range(len(nums_as_int)) if not index % 2 == 0]

result = ""
for index, val in enumerate(not_number_list):
    for el_take_list in take_list:
        if el_take_list == 0:
            pass
        result += el_take_list*not_number_list[val]
        for elem in skip_list:
            el_take_list += elem

a = 5
