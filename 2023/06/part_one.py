with open("data", "r") as file:
    data = [line.removesuffix("\n") for line in file.readlines() if line != "\n"]

times = [int(x) for x in data[0].split()[1:]]
distances = [int(x) for x in data[1].split()[1:]]

res: [int] = []
for t, d in zip(times, distances):
    total = 0
    for seconds in range(0, t):
        travelled = (1 * seconds) * (t - seconds)
        if travelled > d:
            total += 1
    res.append(total)

product = 1
for r in res:
    product *= r

print(product)
