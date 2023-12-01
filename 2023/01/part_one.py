def clean(string: str) -> str:
    return string.replace("\n", "")


if __name__ == "__main__":
    with open("data", "r") as file:
        data = [clean(x) for x in file.readlines()]

    strings = []
    for d in data:
        temp = ""
        for char in d:
            if char.isdigit():
                temp += char
        strings.append(temp)

    res = []
    for r in strings:
        number = str(r[0]) + str(r[len(r) - 1])
        res.append(int(number))

    print(sum(res))
