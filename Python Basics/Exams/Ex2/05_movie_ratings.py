sum_all_ratings = 0
movie_number = int(input())

highest_rating = 0
highest_rated_title = ''

lowest_rating = 11
lowest_rated_title = ''

current_rating = 0
current_title = ''

for _ in range(movie_number):
    movie_title = input()
    movie_rating = float(input())
    sum_all_ratings += movie_rating

    if movie_rating >= highest_rating:
        highest_rating = movie_rating
        highest_rated_title = movie_title

    if movie_rating <= lowest_rating:
        lowest_rating = movie_rating
        lowest_rated_title = movie_title

average_rating = sum_all_ratings / movie_number

print(f'{highest_rated_title} is with highest rating: {highest_rating:.1f}')
print(f'{lowest_rated_title} is with lowest rating: {lowest_rating:.1f}')
print(f'Average rating: {average_rating:.1f}')
