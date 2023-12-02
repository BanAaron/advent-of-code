from part_one import clean

numbers = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine",
}

if __name__ == "__main__":
    with open("data", "r") as file:
        data = [clean(x) for x in file.readlines()]

    converted = []
    for d in data:
        for k, v in numbers.items():
            d = d.replace(k, str(v))
        converted.append(d)

    print(converted)
    data = converted
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
