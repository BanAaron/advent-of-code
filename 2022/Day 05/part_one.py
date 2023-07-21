import re

with open("data", "r") as read_file:
    instructions: list[list[int]] = [
        re.findall(r"\d+", line.strip())
        for line in read_file.readlines()
        if line.startswith("move")
    ]

boxes: list[list[str]] = [
    ["M", "J", "C", "B", "F", "R", "L", "H"],
    ["Z", "C", "D"],
    ["H", "J", "F", "C", "N", "G", "W"],
    ["P", "J", "D", "M", "T", "S", "B"],
    ["N", "C", "D", "R", "J"],
    ["W", "L", "D", "Q", "P", "J", "G", "Z"],
    ["P", "Z", "T", "F", "R", "H"],
    ["L", "V", "M", "G"],
    ["C", "B", "G", "P", "F", "Q", "R", "J"],
]


def move_boxes(
    amount_to_move: int,
    source: int,
    target: int,
    stacks: list[list[str]]
) -> list[list[str]]:
    """
    moves boxes between different stacks
    :param amount_to_move: the mount of boxes to move from the stack
    :param source: index of the stack you want to take boxes from
    :param target: index of the stack you want to transfer boxes top
    :param stacks: the data you want to manipulate
    :return: stack_of_boxes with the transformations applied
    """
    stacks = stacks[:]
    for x in range(amount_to_move):
        if len(stacks[source - 1]) == 0:
            # if there are no boxes on the from_stack skip this iteration and go on to the next one
            continue
        top_box: str = stacks[source - 1].pop()
        stacks[target - 1].append(top_box)
    return stacks


if __name__ == "__main__":
    for instruction in instructions:
        amount, fr, to = [int(x) for x in instruction]
        boxes = move_boxes(amount, fr, to, boxes)

    print(
        "".join([x.pop() for x in boxes])
    )
