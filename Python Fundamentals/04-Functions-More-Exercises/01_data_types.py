def data_types(first_entry: str, second_entry):
    if first_entry == "int":
        return int(second_entry) * 2

    if first_entry == "real":
        return f"{float(second_entry) * 1.5:.2f}"

    if first_entry == "string":
        return f"${second_entry}$"

first_command = input()
second_command = input()
print(data_types(first_entry=first_command, second_entry=second_command))