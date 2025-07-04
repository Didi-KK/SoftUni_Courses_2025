# До команда "STOP" получавате заглавия на любими ваши филми.
# Най-добрият
# филм за вас ще бъде този, който има най-много точки.
# Точките се изчисляват като сбор от ASCII стойностите
# на символите в заглавието на филма. (няма да има случай, в който имаме два филма с равен брой точки)
# При изчислението на точките трябва да се има предвид следното:
# • За всяка малка буква в заглавието, от сумата трябва да се извади два пъти дължината на заглавието
# на филма.
# • За всяка главна буква в заглавието, от сумата трябва да се извади дължината на заглавието на
# филма.
best_movie_score = 0
current_movie_score = 0
for _ in range(7):
    command = input()
    if command == 'STOP':
        break
    movie_title = command
    for letter in movie_title:
        current_movie_score += ord(letter)




# От конзолата се четат редове до команда "STOP" или до достигането на лимита от 7 филма:
# • Заглавие на филм – текст;
# Изход
# На конзолата да се отпечата:
# • Ако сте достигнали лимита от 7 филма трябва да отпечатате:
# "The limit is reached."
# Да се отпечата най-добрият филм за вас:
# "The best movie for you is {заглавие на филм} with {сума на символите} ASCII sum."