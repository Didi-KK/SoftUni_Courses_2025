money_as_string = input().split(", ")
beggars = int(input())
money_as_integer = []

for money in money_as_string:
    money_as_integer.append(int(money))

beggars_money = []
start_index = 0

for current_beggar in range(beggars):
    current_beggar_sum = 0
    for index in range(start_index, len(money_as_integer), beggars):
        current_beggar_sum += money_as_integer[index]
    beggars_money.append(current_beggar_sum)
    start_index += 1

print(beggars_money)
