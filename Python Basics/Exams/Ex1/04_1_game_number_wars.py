player_one_points = 0
player_two_points = 0

player_one = input()
player_two = input()

end_of_game = False

entry = int(input())

while entry != 'End of game':
    
    player_one_card = int(entry)
    player_two_card = int(input())
    
    if player_one_card == player_two_card:
        end_of_game = True
        print('Number wars!')
        
        player_one_card = int(input())
        player_two_card = int(input())
        
        if player_one_card > player_two_card:
            print(f'{player_one} is winner with {player_one_points} points')
        elif player_two_card > player_one_card:
            print(f'{player_two} is winner with {player_two_points} points')
        break
    
    if player_one_card > player_two_card:
        player_one_points += player_one_card - player_two_card
    else:
        player_two_points += player_two_card - player_one_card
    
    entry = input()

if not end_of_game:
    print(f'{player_one} has {player_one_points} points')
    print(f'{player_two} has {player_two_points} points')
