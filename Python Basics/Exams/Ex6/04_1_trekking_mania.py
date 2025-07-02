group_number = int(input())

musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

for _ in range(group_number):
    group_members_count = int(input())
    if group_members_count <= 5:
        musala += group_members_count

    elif group_members_count <= 12:
        montblanc += group_members_count

    elif group_members_count <= 25:
        kilimanjaro += group_members_count

    elif group_members_count <= 40:
        k2 += group_members_count

    else:
        everest += group_members_count

all_participants = (musala + montblanc
                    + kilimanjaro + k2 + everest)

musala_p = musala / all_participants * 100
montblanc_p = montblanc / all_participants * 100
kilimanjaro_p = kilimanjaro / all_participants * 100
k2_p = k2 / all_participants * 100
everest_p = everest / all_participants * 100

print(f'{musala_p:.2f}%')
print(f'{montblanc_p:.2f}%')
print(f'{kilimanjaro_p:.2f}%')
print(f'{k2_p:.2f}%')
print(f'{everest_p:.2f}%')

