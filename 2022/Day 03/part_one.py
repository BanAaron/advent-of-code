from string import ascii_lowercase, ascii_uppercase


def find_duplicate_char(*args: str) -> str:
    args: list[str] = list(args)
    first_string: str = args.pop(0)
    for char in first_string:
        for arg in args:
            if char in arg:
                return char


def get_character_score(char: str) -> int:
    """
    Lowercase characters a through z have the score 1 through 26.
    Uppercase characters A through Z have the score 27 through 52.
    :param char: A single character
    :return: 1-52
    """
    charset: str = ascii_lowercase + ascii_uppercase
    if len(char) != 1 or char not in charset:
        raise ValueError(f"{char} is not a valid character.")
    return charset.find(char) + 1


if __name__ == "__main__":
    with open("rucksacks", "r") as read_file:
        lines: list[str] = read_file.readlines()

    score: int = 0
    for line in lines:
        halfway: int = len(line) // 2
        first_half: str = line[:halfway]
        second_half: str = line[halfway:]
        duplicate_char: str = find_duplicate_char(first_half, second_half)
        score += get_character_score(duplicate_char)

    print(score)
