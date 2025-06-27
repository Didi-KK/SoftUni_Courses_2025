guests = int(input())
budget = float(input())

brioche = 4.00
egg = 0.45

if guests % 3 == 0:
    brioche_num = guests / 3
else:
    brioche_num = guests // 3 + 1
egg_num = guests * 2
expenses = brioche_num * brioche + egg_num * egg
diff = budget - expenses
if expenses <= budget:
    print(f'Lyubo bought {brioche_num} Easter bread and {egg_num} eggs.'
          f'\nHe has {diff:.2f} lv. left.')
else:
    print(f'Lyubo doesn\'t have enough money.'
          f'\n'
          f'He needs {abs(diff):.2f} lv. more.')
