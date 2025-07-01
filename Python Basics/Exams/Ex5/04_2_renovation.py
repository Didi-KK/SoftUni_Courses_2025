from math import ceil
is_tired = False
wall_height = int(input())
wall_width = int(input())
percent_no_paint = int(input())
area_to_paint = ceil((4 * wall_height * wall_width * (1 - percent_no_paint / 100)))
paint_done = area_to_paint
command = input()

while command != 'Tired!':
    paint_liters = int(command)
    paint_done -= paint_liters
    if paint_done < 0:
        print(f'All walls are painted and you have {(abs(paint_done))} l paint left!')
        break
    if paint_done == 0:
        print(f'All walls are painted! Great job, Pesho!')
        break
    command = input()
    if command == 'Tired!':
        is_tired = True
        if is_tired:
            print(f'{(abs(paint_done))} quadratic m left.')
            break




