# year = int(input())
# special = False
# while not special:
#     year += 1
#     year_as_string = str(year)
#     if len(year_as_string) == len(set(year_as_string)):
#         special = True
#         break
# print(year)

year = int(input())
current_year = year

while True:
    current_year += 1
    year_str = str(current_year)

    if len(year_str) == len(set(year_str)):
        print(current_year)
        break