elements = input().split()
moves = 0
while True:
    command = input()
    if command =="end":
        break
    index1, index2 = map(int, command.split())
    moves += 1
    if index1 == index2 or index1 not in range(len(elements)) or index2 not in range(len(elements)):
        middle_index = len(elements) // 2
        elements.insert(middle_index, f"-{moves}a")
        elements.insert(middle_index, f"-{moves}a")
        print(f"Invalid input! Adding additional elements to the board")
    else:
        if elements[index1] == elements[index2]:
            element = elements[index1]
            print(f"Congrats! You have found matching elements - {element}!")
            elements.pop(max(index1, index2))
            elements.pop(min(index1, index2))
        else:
            print("Try again!")
    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break
if len(elements) > 0:
    print(f"Sorry you lose :(\n{' '.join(elements)}")

