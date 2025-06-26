country = input()
apparatus = input()

difficulty = 0.0
performance = 0.0
if country == 'Russia':
    if apparatus == 'ribbon':
        difficulty = 9.100
        performance = 9.400
    elif apparatus == 'hoop':
        difficulty = 9.300
        performance = 9.800
    elif apparatus == 'rope':
        difficulty = 9.600
        performance = 9.000
if country == 'Bulgaria':
    if apparatus == 'ribbon':
        difficulty = 9.600
        performance = 9.400
    elif apparatus == 'hoop':
        difficulty = 9.550
        performance = 9.750
    elif apparatus == 'rope':
        difficulty = 9.500
        performance = 9.400
if country == 'Italy':
    if apparatus == 'ribbon':
        difficulty = 9.200
        performance = 9.500
    elif apparatus == 'hoop':
        difficulty = 9.450
        performance = 9.350
    elif apparatus == 'rope':
        difficulty = 9.700
        performance = 9.150
total_score = difficulty + performance
percentage_score = (20 - total_score) / 20 * 100
print(f'The team of {country} get {total_score:.3f} on {apparatus}.')
print(f'{percentage_score:.2f}%')

