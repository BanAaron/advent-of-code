from part_one import clean

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

# the problem with this one is that some numbers in string form can overlap
# to create two different numbers. For example eightwothree == 823, but using
# doing a replacement on the string values would remove the eight

# probably the best solution is to use a sliding window to break up the string
# into pieces
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
