with open("data", "r") as file:
    data = file.read()
    cards = data.splitlines()

# store the number of cards in a dict
number_of_cards: dict[int, int] = {}

# we start with one of each card, so we can default to 1
for x in range(len(cards)):
    number_of_cards[x + 1] = 1

# go through each game
for i, card in enumerate(cards, 1):
    # get the data in the right format
    card = card.split(":")
    numbers = card[1].split("|")
    winning_numbers = numbers[0].split()
    my_numbers = numbers[1].split()

    # count how many winning numbers we have
    count = 0
    for number in my_numbers:
        if number in winning_numbers:
            count += 1

    # add a card for each of the matches
    for x in range(i + 1, i + 1 + count):
        number_of_cards[x] += number_of_cards[i]


print(number_of_cards)
print(sum(number_of_cards.values()))
