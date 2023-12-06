with open("data", "r") as file:
    data = [line.removesuffix("\n") for line in file.readlines() if line != "\n"]

time = int(data[0].split(":")[1].replace(" ", ""))
distance = int(data[1].split(":")[1].replace(" ", ""))

total = 0
for seconds in range(0, time):
    travelled = (1 * seconds) * (time - seconds)
    if travelled > distance:
        total += 1

print(total)
