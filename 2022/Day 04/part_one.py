if __name__ == "__main__":
    with open("data", "r") as read_file:
        number_ranges = [line.strip() for line in read_file.readlines()]

    score = 0
    for ranges in number_ranges:
        left, right = [list(map(int, x.split("-"))) for x in ranges.split(",")]

        if (left[0] <= right[0] and left[1] >= right[1]) or (
            right[0] <= left[0] and right[1] >= left[1]
        ):
            score += 1

    print(score)
