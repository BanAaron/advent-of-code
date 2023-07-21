from read_data import calories

calories_per_elf: list[int] = []
total: int = 0

for calorie in calories:
    if calorie == "":
        calories_per_elf.append(total)
        total = 0
    else:
        total += int(calorie)

print(max(calories_per_elf))
