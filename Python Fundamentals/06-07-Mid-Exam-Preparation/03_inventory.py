collecting_items = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break
    action, item = command.split(" - ")
    if action == "Collect":
        if item not in collecting_items:
            collecting_items.append(item)
    elif action == "Drop":
        if item in collecting_items:
            collecting_items.remove(item)
    elif action == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in collecting_items:
            index = collecting_items.index(old_item)
            collecting_items.insert(index + 1, new_item)
    elif action == "Renew":
        if item in collecting_items:
            index = collecting_items.index(item)
            collecting_items.pop(index)
            collecting_items.append(item)

print(", ".join(collecting_items))