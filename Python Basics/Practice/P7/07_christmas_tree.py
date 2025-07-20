christmas_tree_size = int(input())

for i in range(0, christmas_tree_size+1):
    row = f"{' ' * (christmas_tree_size - i)}{'*' * i} | {'*' * i}{' ' * (christmas_tree_size - i)}"

    print(row)
