movie_title = input()
cinema_hall = input()
tickets_sold = int(input())

tickets_price = 0.0

if movie_title == 'A Star Is Born':
    if cinema_hall == 'normal':
        tickets_price = 7.50  * tickets_sold
    elif cinema_hall == 'luxury':
        tickets_price = 10.50  * tickets_sold
    elif cinema_hall == 'ultra luxury':
        tickets_price = 13.50  * tickets_sold
        
elif movie_title == 'Bohemian Rhapsody':
    if cinema_hall == 'normal':
        tickets_price = 7.35 * tickets_sold
    elif cinema_hall == 'luxury':
        tickets_price = 9.45  * tickets_sold
    elif cinema_hall == 'ultra luxury':
        tickets_price = 12.75  * tickets_sold
        
elif movie_title == 'Green Book':
    if cinema_hall == 'normal':
        tickets_price = 8.15  * tickets_sold
    elif cinema_hall == 'luxury':
        tickets_price = 10.25  * tickets_sold
    elif cinema_hall == 'ultra luxury':
        tickets_price = 13.25  * tickets_sold

elif movie_title == 'The Favourite':
    if cinema_hall == 'normal':
        tickets_price = 8.75  * tickets_sold
    elif cinema_hall == 'luxury':
        tickets_price = 11.55  * tickets_sold
    elif cinema_hall == 'ultra luxury':
        tickets_price = 13.95  * tickets_sold
        

print(f'{movie_title} -> {tickets_price:.2f} lv.')