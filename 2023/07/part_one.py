from collections import Counter
from dataclasses import dataclass


@dataclass
class Hand:
    def __init__(self, cards: str, score: int, hand_type: str):
        self.cards = cards
        self.score = score
        self.hand_type = hand_type

    def __repr__(self):
        return f"{self.cards}, {self.score}, {self.hand_type}"


card_types = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
hand_type_order = ["five", "four", "full", "three", "two", "one", "high"]


def get_hand_type(hand_string: str) -> str:
    count = Counter(hand_string)
    length = len(count)
    maximum = max(count.values())

    if maximum == 5 and length == 1:
        return "five"
    if maximum == 4 and length == 2:
        return "four"
    if maximum == 3 and length == 2:
        return "full"
    if maximum == 3 and length == 3:
        return "three"
    if maximum == 2 and length == 3:
        return "two"
    if maximum == 2 and length == 4:
        return "one"
    if maximum == 1 and length == 5:
        return "high"


if __name__ == '__main__':
    hands: [Hand] = []

    with open("data", "r") as file:
        data = [x.removesuffix("\n").split() for x in file.readlines()]

    for d in data:
        hand = d[0]
        value = int(d[1])
        hand_type = get_hand_type(hand)
        hands.append(Hand(hand, value, hand_type))


    def custom_sort(hand):
        return (
            hand_type_order.index(hand.hand_type),
            [card_types.index(card) for card in hand.cards],
            hand.score
        )


    sorted_hands = sorted(hands, key=custom_sort, reverse=True)

    score: int = 0
    for idx, hand in enumerate(sorted_hands, start=1):
        print(f"Rank {idx}: {hand}")
        score += idx * hand.score

    print(score)
