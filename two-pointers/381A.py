number_of_cards = input()

cards = list(map(int, input().split()))
sereja = 0
dima = 0

alternate_turns = 0

while cards:
    greater_value = max(cards[0], cards[-1])
    if alternate_turns % 2 == 0:
        sereja += greater_value
    else:
        dima += greater_value
    alternate_turns = alternate_turns + 1
    cards.remove(greater_value)

print(sereja, dima)
