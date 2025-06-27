brioche = int(input())
dozen_eggs = int(input())
cookies_kg = int(input())

brioche_cost = brioche * 3.20
dozen_eggs_cost = dozen_eggs * 4.35
cookies_kg_cost = cookies_kg * 5.40
egg_dye_cost = 12 * 0.15 * dozen_eggs
expenses = brioche_cost + dozen_eggs_cost + cookies_kg_cost + egg_dye_cost

print(f'{expenses:.2f}')
