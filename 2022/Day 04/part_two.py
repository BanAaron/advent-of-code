if __name__ == "__main__":
    with open("data", "r") as read_file:
        number_ranges = [line.strip() for line in read_file.readlines()]

    score = 0
    for ranges in number_ranges:
        left: list[int]
        right: list[int]
        left, right = [list(map(int, x.split("-"))) for x in ranges.split(",")]

        left_range = list(range(left[0], left[1] + 1))
        right_range = list(range(right[0], right[1] + 1))

        for x in left_range:
            if x in right_range:
                score += 1
                break

    print(score)
