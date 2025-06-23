open_tabs = int(input())
salary = int(input())


for _ in range(open_tabs):
    browser_tab = input()

    if browser_tab == 'Facebook':
        salary -= 150
        if salary <= 0:
            break
    elif browser_tab == 'Instagram':
        salary -= 100
        if salary <= 0:
            break
    elif browser_tab == 'Reddit':
        salary -= 50
        if salary <= 0:
            break

if salary <= 0:
    print(f'You have lost your salary.')
else:
    print(f'{salary}')
    