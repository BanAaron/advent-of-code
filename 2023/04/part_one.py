from math import floor

with open("data", "r") as file:
    data = file.read()
    cards = data.splitlines()

scores: list[int] = []

for card in cards:
    card = card.split(":")
    numbers = card[1].split("|")
    winning_numbers = numbers[0].split()
    my_numbers = numbers[1].split()

    count = -1
    for i, n in enumerate(my_numbers):
        if n in winning_numbers:
            count += 1

    score = floor(2**count)
    scores.append(score)

print(sum(scores))
