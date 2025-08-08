my_list = input().split()
every_next = int(input())

my_list_gone_by_number = []
index = 0
while my_list:
    index = (index + every_next - 1) % len(my_list)
    my_list_gone_by_number.append(my_list.pop(index))

print(f"[{','.join(my_list_gone_by_number)}]")
