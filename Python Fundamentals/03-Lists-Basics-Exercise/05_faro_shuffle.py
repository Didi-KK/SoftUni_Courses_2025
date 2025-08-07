deck_of_cards = input().split(" ")
count_of_faro_shuffles = int(input())

faro_shuffled_deck_of_cards = deck_of_cards
for current_shuffle in range(count_of_faro_shuffles):

    first_half = faro_shuffled_deck_of_cards[: len(faro_shuffled_deck_of_cards) // 2]
    second_half = faro_shuffled_deck_of_cards[len(faro_shuffled_deck_of_cards) // 2:]
    faro_shuffled_deck_of_cards = []

    for index in range(len(deck_of_cards) // 2):
        faro_shuffled_deck_of_cards.append(first_half[index])
        faro_shuffled_deck_of_cards.append(second_half[index])

print(faro_shuffled_deck_of_cards)
