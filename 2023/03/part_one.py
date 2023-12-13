def check_adjacent(matrix: list[list], x: int, y: int) -> list:
    directions = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i, j) != (0, 0):
                directions.append((i, j))

    neighbors = []
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]):
            neighbors.append(matrix[new_x][new_y])

    return neighbors


def contains_symbol(lst: list) -> bool:
    return any(character not in ".0123456789" for character in lst)


if __name__ == "__main__":
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

    numbers: list[int] = []
    store: str = ""
    adjacent: list[bool] = []

    for x in range(height):
        # edge case when the number ends at the end of a line
        if store.isdigit() and contains_symbol(adjacent):
            numbers.append(int(store))
            store = ""
            adjacent = []

        for y in range(width):
            char = arr[x][y]
            if char.isdigit():
                store += char
                adjacent += check_adjacent(arr, x, y)
            elif store.isdigit() and contains_symbol(adjacent):
                numbers.append(int(store))
                store = ""
                adjacent = []
            else:
                store = ""
                adjacent = []

    print(sum(numbers))
