movie_tittle = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
cinema_percentage = int(input())

profit = days * tickets * ticket_price * (100 - cinema_percentage) / 100

print(f'The profit from the movie {movie_tittle} is {profit:.2f} lv.')
