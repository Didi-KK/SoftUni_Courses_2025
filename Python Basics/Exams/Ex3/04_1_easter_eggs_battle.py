player_one_eggs = int(input())
player_two_eggs = int(input())

while player_one_eggs > 0 and player_two_eggs > 0:
    entry = input()
    if entry == 'End':
        print(f"Player one has {player_one_eggs} eggs left."
              f"\nPlayer two has {player_two_eggs} eggs left.")
        break
        
    elif entry == 'one':
        player_two_eggs -= 1
    elif entry == 'two':
        player_one_eggs -= 1
        
if player_one_eggs <= 0:
    print(f"Player one is out of eggs. Player two has {player_two_eggs} eggs left.")
            
elif player_two_eggs <= 0:
    print(f"Player two is out of eggs. Player one has {player_one_eggs} eggs left.")


