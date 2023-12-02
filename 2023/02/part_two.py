from re import findall

# I gave in to the regex demon
if __name__ == '__main__':
    with open("data", "r") as file:
        data = file.readlines()

    powers: list[int] = []
    reds: list[int] = []
    greens: list[int] = []
    blues: list[int] = []

    for line in data:
        # red
        pattern = fr'(\d+)\s+red'
        matches = findall(pattern, line)
        reds.append(max([int(x) for x in matches]))
        # green
        pattern = fr'(\d+)\s+green'
        matches = findall(pattern, line)
        greens.append(max([int(x) for x in matches]))
        # blue
        pattern = fr'(\d+)\s+blue'
        matches = findall(pattern, line)
        blues.append(max([int(x) for x in matches]))

    for i in range(len(reds)):
        powers.append(reds[i] * greens[i] * blues[i])

    print(sum(powers))
