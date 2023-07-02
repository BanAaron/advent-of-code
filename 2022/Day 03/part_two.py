from part_one import get_character_score, find_duplicate_char


if __name__ == '__main__':
    with open('rucksacks', 'r') as read_file:
        lines: list[str] = read_file.readlines()

    score: int = 0
    chunk_size: int = 3
    for x in range(0, len(lines), chunk_size):
        chunk: list[str] = lines[x:x + chunk_size]
        chunk = [c.removesuffix('\n') for c in chunk]
        duplicate_char: str = find_duplicate_char(*chunk)
        score += get_character_score(duplicate_char)

    print(score)
