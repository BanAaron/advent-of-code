with open("data", "r") as file:
    file = [l.removesuffix("\n") for l in file.readlines()]

pattern = file.pop(0)
file.pop(0)

store: dict[str, tuple[str, str]] = {}

for x in file:
    location = x.split()[0]
    l = x.split(",")[0][-3:]
    r = x.split(",")[1][-4:-1]
    store[location] = (l, r)

steps = 0
curr = "AAA"
while curr != "ZZZ":
    for dir in pattern:
        if dir == "L":
            curr = store[curr][0]
        elif dir == "R":
            curr = store[curr][1]
        steps += 1

print(steps)
