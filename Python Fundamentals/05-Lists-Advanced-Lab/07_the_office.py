employees = input().split(' ')
happiness_factor = int(input())

how_happy = list(map(lambda x: int(x) * happiness_factor, employees))

happiness = list(filter(lambda x: x >= (sum(how_happy) / len(how_happy)), how_happy))

happy_count = len(happiness)
total_count = len(employees)
if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
