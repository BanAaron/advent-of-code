with open("calories", "r") as read_file:
    calories: list[str] = [line.strip() for line in read_file.readlines()]
