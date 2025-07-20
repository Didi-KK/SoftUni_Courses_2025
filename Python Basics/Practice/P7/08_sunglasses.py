sunglasses_size = int(input())
top_row = ''
for i in range(1, sunglasses_size + 1):
    if i == 1:
        top_row = (f"{'*' * (sunglasses_size * 2)}{' ' * sunglasses_size}"
                   f"{'*' * (sunglasses_size * 2)}")
        print(top_row)
for i in range(sunglasses_size - 2):

    if i == (sunglasses_size - 1) // 2 - 1:
        row = (f"*{'/' * (2 * (sunglasses_size - 1))}*{'|' * sunglasses_size}*"
               f"{'/' * (2 * (sunglasses_size - 1))}*")
        print(row)
    else:
        row = f"*{'/' * (2 * (sunglasses_size - 1))}*{' ' * sunglasses_size}*{'/' * (2 * (sunglasses_size - 1))}*"
        print(row)

for i in range(1, sunglasses_size + 1):
    if i == sunglasses_size:
        print(top_row)
