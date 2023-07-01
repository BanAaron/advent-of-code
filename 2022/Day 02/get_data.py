with open("playbook", "r") as read_file:
    lines: list[str] = read_file.readlines()
    playbook: list[list[str]] = [line.removesuffix("\n").split(" ") for line in lines]
