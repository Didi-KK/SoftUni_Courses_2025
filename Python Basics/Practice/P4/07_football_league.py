stadium_capacity = int(input())
fan_count = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for i in range(fan_count):
    sector = input()
    if sector == 'A':
        sector_a += 1
    elif sector == 'B':
        sector_b += 1
    elif sector == 'V':
        sector_v += 1
    elif sector == 'G':
        sector_g += 1

all_fans = sector_a + sector_b + sector_g + sector_v

sector_a_p = sector_a / fan_count * 100
sector_b_p = sector_b / fan_count * 100
sector_v_p = sector_v / fan_count * 100
sector_g_p = sector_g / fan_count * 100
stadium_p = all_fans / stadium_capacity * 100

print(f'{sector_a_p:.2f}%'
      f'\n{sector_b_p:.2f}%'
      f'\n{sector_v_p:.2f}%'
      f'\n{sector_g_p:.2f}%'
      f'\n{stadium_p:.2f}%')
