cards = input().split()
n_shuffles = int(input())

top_card = cards[0]
bottom_card = cards[-1]

half = len(cards) // 2

left_cards = []
right_cards = []

shuffle_cards = []

for n_shuffles in range(n_shuffles):
    for index in range(1, half):
        left_cards.append(cards[index])

    for index in range(half, len(cards) - 1):
        right_cards.append(cards[index])

    for index in range(len(left_cards)):
        shuffle_cards.append(right_cards[index])
        shuffle_cards.append(left_cards[index])

    cards = shuffle_cards.copy()
    cards.append(bottom_card)
    cards.insert(0, top_card)
    shuffle_cards = []
    left_cards = []
    right_cards = []

print(cards)