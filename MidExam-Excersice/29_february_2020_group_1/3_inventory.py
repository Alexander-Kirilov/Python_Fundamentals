def collect(items, i):
    if i not in items:
        items.append(item)
    return items


def drop(items, i):
    if i in items:
        items.remove(i)
    return items


def combine_items(items, i):
    old_item = i.split(":")[0]
    new_item = i.split(":")[1]
    if old_item in items:
        index_old_item = items.index(old_item)
        index_new_item = index_old_item+1
        items.insert(index_new_item, new_item)
    return items


def renew(items, i):
    if i in items:
        items.remove(i)
        items.append(i)
    return items


journal = input().split(", ")

data = input()

while not data == "Craft!":
    command, item = data.split(" - ")

    if command == "Collect":
        journal = collect(journal, item)
    elif command == "Combine Items":
        journal = combine_items(journal, item)
    elif command == "Renew":
        journal = renew(journal, item)
    elif command == "Drop":
        journal = drop(journal, item)

    data = input()

print(", ".join(journal))
