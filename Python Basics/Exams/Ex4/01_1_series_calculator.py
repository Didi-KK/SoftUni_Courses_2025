from math import floor

series = input()
seasons = int(input())
episodes = int(input())
duration = float(input())

add_episode = seasons * 10
ads = seasons * 0.20 * duration * episodes

time = seasons * episodes * duration + ads + add_episode

print(f'Total time needed to watch the {series} series is {floor(time)} minutes.')
