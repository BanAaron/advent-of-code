with open("data", "r") as file:
    file = [line.removesuffix("\n") for line in file.readlines()]

pattern = file.pop(0)
file.pop(0)

store: dict[str, tuple[str, str]] = {}

for x in file:
    location = x.split()[0]
    left = x.split(",")[0][-3:]
    right = x.split(",")[1][-4:-1]
    store[location] = (left, right)

steps = 0
curr = "AAA"
while curr != "ZZZ":
    for direction in pattern:
        if direction == "L":
            curr = store[curr][0]
        elif direction == "R":
            curr = store[curr][1]
        steps += 1

print(steps)
