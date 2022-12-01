
with open("day1.txt") as f:
    elf = 0
    elves = []
    for line in f:
        if line == "\n":
            elves.append(elf)
            elf = 0
        else:
            elf += int(line)
    elves = sorted(elves)
    print(elves[-1])
    print(sum(elves[-3:]))