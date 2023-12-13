import re

# I hate everything about this
# I gave in to the regex demon
if __name__ == "__main__":
    with open("data", "r") as file:
        data = file.readlines()

    RED_MAX = 12
    GREEN_MAX = 13
    BLUE_MAX = 14

    res: list[int] = []

    for i, line in enumerate(data):
        game_id = i + 1

        impossible = False
        for s in line.split(";"):
            red_pattern = r"(\d+)\s+red"
            red_matches = re.findall(red_pattern, s)
            reds = sum([int(x) for x in red_matches])

            green_pattern = r"(\d+)\s+green"
            green_matches = re.findall(green_pattern, s)
            greens = sum([int(x) for x in green_matches])

            blue_pattern = r"(\d+)\s+blue"
            blue_matches = re.findall(blue_pattern, s)
            blues = sum([int(x) for x in blue_matches])

            # would be more efficient to check each as we go, but I am lazy
            if reds > RED_MAX or greens > GREEN_MAX or blues > BLUE_MAX:
                impossible = True
                break

        if impossible:
            continue
        else:
            res.append(game_id)

    print(sum(res))
