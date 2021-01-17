users = input().split(", ")

for user in users:
    if 3 <= len(user) <= 16 and len(user) == len([char for char in user if ord(char) in range(48, 58) or ord(char) in range(65, 91) or ord(char) in range(97, 123) or ord(char) == 45 or ord(char) == 95]):
        print(user)

# Кратък вариант:
#
# names = input().split(", ")
#
# for name in names:
#     if 3 <= len(name) <= 16 and name.isalnum() or '_' in name or '-' in name:
#         print(name)