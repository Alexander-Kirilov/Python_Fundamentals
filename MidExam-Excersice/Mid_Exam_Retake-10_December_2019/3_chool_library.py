book_shelf = input().split("&")

command = input()
while not command == "Done":
    action, book_name = command.split(" | ", 2)

    if action == "Add Book":
        if book_name in book_shelf:
            book_shelf.insert(0, book_name)
    elif action == "Take Book":
        if book_name in book_shelf:
            book_shelf.remove(book_name)
    elif action == "Swap Books":
        book_1, book_2 = book_name.split(" | ")
        if book_1 and book_2 in book_shelf:
            book_1_index = book_shelf.index(book_1)
            book_2_index = book_shelf.index(book_2)



    command = input()
