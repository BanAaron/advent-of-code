def check_adjacent(x: int, y: int) -> bool:
    # cardinal
    # up
    pass

    # diagonal


if __name__ == '__main__':
    with open("data", "r") as file:
        data = file.readlines()
        data = [x.replace("\n", "").strip() for x in data]

    # get the dimension of our array
    height: int = len(data)
    width: int = len(data[0])
    # make a 2d array
    arr: list[list[str]] = [["" for i in range(height)] for j in range(width)]

    # insert our data into the array
    for x, r in enumerate(data):
        for y, c in enumerate(r):
            arr[x][y] = c

    print(data, "\n")

    numbers: list[int] = []
    store: str = ""

    for x in range(height):
        for y in range(width):
            char = arr[x][y]
            if char.isdigit():
                store += char
            elif len(store) > 1:
                numbers.append(int(store))
                store = ""

    print(numbers)
