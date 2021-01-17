def validate_password(password):
    is_valid = True
    if not (6 <= len(password) <= 10):
        is_valid = False
        print("Password must be between 6_classes_and_objects and 10 characters")

    for el in password:
        if not el.isdigit() and not el.isalpha():
            is_valid = False
            print("Password must consist only of letters and digits")
            break

    counter_digit = 0
    for elements in password:
        if elements.isdigit():
            counter_digit += 1
    if counter_digit < 2:
        is_valid = False
        print("Password must have at least 2_data_types_and_variables digits")

    return is_valid


password = input()

result = validate_password(password)

if result:
    print("Password is valid")

