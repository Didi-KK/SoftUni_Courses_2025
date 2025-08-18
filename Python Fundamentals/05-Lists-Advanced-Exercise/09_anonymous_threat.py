def merge_data(incoming_info: list, starting_index: int, ending_index: int) -> list:
    starting_index = max(0, starting_index)
    ending_index = min(ending_index, len(incoming_info) - 1)
    incoming_info_merged = "".join(incoming_info[starting_index:ending_index + 1])
    incoming_info_modified = incoming_info[:starting_index] + [incoming_info_merged] + incoming_info[ending_index + 1:]
    return incoming_info_modified


def divide_data(incoming_info: list, target_index: int, partition: int) -> list:
    target_element = incoming_info[target_index]
    target_element_len = len(target_element)
    partition_size = target_element_len // partition
    new_element = [target_element[i * partition_size: (i + 1) * partition_size] for i in range(partition - 1)]
    new_element.append(target_element[(partition - 1) * partition_size:])
    incoming_info_modified = incoming_info[:target_index] + new_element + incoming_info[target_index + 1:]
    return incoming_info_modified


incoming_data = input().split()
command = input().split()

while len(command) > 1:
    action = command[0]
    if action == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        incoming_data = merge_data(incoming_data, start_index, end_index)

    elif action == "divide":
        element_index = int(command[1])
        parts = int(command[2])
        if parts > 0:
            incoming_data = divide_data(incoming_data, element_index, parts)

    command = input().split()

print(*incoming_data)
